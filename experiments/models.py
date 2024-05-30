from django.db import models
from django.conf import settings

class Experiment(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiments"
    )
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

class Population(models.Model):
    experiment_id = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    game_seed = models.IntegerField()
    generation_nr  = models.IntegerField(default=1)

class Individual(models.Model):
    population_id = models.ForeignKey(Population, on_delete=models.CASCADE)
    # initial declaration of genotype as string with max len 100, can be modified later
    genotype = models.CharField(max_length=100)
    # initial declaration of fitness in individual, can be deleted later
    fitness = models.FloatField()

class GameIteration(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    position = models.FloatField()
    angle = models.FloatField()