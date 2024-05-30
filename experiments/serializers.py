from rest_framework import serializers
from .models import Experiment, Population, Individual, GameIteration

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = '__all__'

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = '__all__'

class GameIterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameIteration
        fields = '__all__'
