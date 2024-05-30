from django.shortcuts import render
from rest_framework import viewsets
from .models import Experiment, Population, Individual, GameIteration
from .serializers import ExperimentSerializer, PopulationSerializer, IndividualSerializer, GameIterationSerializer

class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

class PopulationViewSet(viewsets.ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class GameIterationViewSet(viewsets.ModelViewSet):
    queryset = GameIteration.objects.all()
    serializer_class = GameIterationSerializer

