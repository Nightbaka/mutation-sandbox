import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers import serialize
import django
from django.db.models import Count, Max, Avg

django.setup()
from .models import Experiment, Population, Individual
from .serializers import ExperimentSerializer
from django.db import connection, models
from asgiref.sync import sync_to_async

@sync_to_async
def get_experiments():
    experiments = Experiment.objects.annotate(
        num_pops = Count('population', distinct=True),
        best_fitness = Max('population__individual__fitness'),
        avg_fitness = Avg('population__individual__fitness')
    )

    exp_payload = []

    for exp in experiments:
        serialized_exp = {
            'id': exp.id,
            'num_pops': exp.num_pops,
            'best_fitness': exp.best_fitness,
            'avg_fitness': exp.avg_fitness
        }
        exp_payload.append(serialized_exp)

    return json.dumps(exp_payload)

@sync_to_async
def get_populations():
    pops = Population.objects.all()
    srl = serialize("json", pops)
    return srl

@sync_to_async
def get_individuals():
    pops = Population.objects.all()
    srl = serialize("json", pops)
    return srl


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(message)

        await self.send(text_data=json.dumps({
            'message': message
        }))


class HistoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        payload = await get_experiments()

        # await self.send(text_data=json.dumps({
        #     'experiments': payload
        # }))

        await self.send(text_data=payload)

