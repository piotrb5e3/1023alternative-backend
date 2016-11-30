from django.db import models
from experiment_settings.models import ExperimentSettings


class Experiment(models.Model):
    settings = models.ForeignKey(ExperimentSettings)
