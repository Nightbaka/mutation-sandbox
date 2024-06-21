import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers import serialize
import django
django.setup()
from .models import Experiment
from .serializers import ExperimentSerializer
from django.db import connection, models
from asgiref.sync import sync_to_async

@sync_to_async
def get_experiments():
    exp = Experiment.objects.all()
    srl = serialize("json", exp)
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


class ExperimentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        payload = await get_experiments()

        # await self.send(text_data=json.dumps({
        #     'experiments': payload
        # }))

        await self.send(text_data=payload)

