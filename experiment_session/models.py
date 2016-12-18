from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ExperimentSession(models.Model):
    STATUS_FINISHED = 'F'
    STATUS_IN_PROGRESS = 'P'
    _STATUS_CHOICES = (
        (STATUS_FINISHED, "Finished"),
        (STATUS_IN_PROGRESS, "In progress"),
    )

    experiment = models.ForeignKey('experiment.Experiment', related_name='sessions')
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)


class Combination(models.Model):
    session = models.ForeignKey(ExperimentSession, related_name='combinations')
    lightset = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(1023)
        )
    )

    class Meta:
        unique_together = ('session', 'lightset')
