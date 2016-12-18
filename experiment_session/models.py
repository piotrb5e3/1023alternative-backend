from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ExperimentSession(models.Model):
    STATUS_FINISHED = 'F'
    STATUS_IN_PROGRESS = 'P'
    _STATUS_CHOICES = (
        (STATUS_FINISHED, "Finished"),
        (STATUS_IN_PROGRESS, "In progress"),
    )

    experiment = models.ForeignKey('experiment.Experiment', related_name='sessions', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    number = models.IntegerField(validators=(MinValueValidator(1),))

    @property
    def progress(self):
        return self.combinations.filter(status=Combination.STATUS_FINISHED).count() / 1023

    def __str__(self):
        return str(self.number)

    class Meta:
        unique_together = ('experiment', 'number',)


class Combination(models.Model):
    STATUS_FINISHED = 'F'
    STATUS_IN_PROGRESS = 'P'
    _STATUS_CHOICES = (
        (STATUS_FINISHED, "Finished"),
        (STATUS_IN_PROGRESS, "In progress"),
    )

    session = models.ForeignKey(ExperimentSession, related_name='combinations', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    lightset = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(1023)
        )
    )

    def __str__(self):
        return str(self.lightset)

    class Meta:
        unique_together = ('session', 'lightset')
