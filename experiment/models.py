from django.db import models
from experiment_session.models import ExperimentSession
from django.core.validators import MinValueValidator


class Experiment(models.Model):
    LIGHTOFF_FIXED = 'fixed'
    LIGHTOFF_WAITING = 'waiting'
    _LIGHTOFF_CHOICES = (
        (LIGHTOFF_FIXED, 'Fixed'),
        (LIGHTOFF_WAITING, 'Waiting')
    )

    AUDIO_NONE = 'none'
    AUDIO_BEEP = 'beep'
    _AUDIO_CHOICES = (
        (AUDIO_NONE, 'None'),
        (AUDIO_BEEP, 'Audible beep on error')
    )

    name = models.CharField(unique=True, max_length=255)

    lightoffmode = models.CharField(
        choices=_LIGHTOFF_CHOICES,
        max_length=30
    )

    lightofftimeout = models.IntegerField(validators=(MinValueValidator(0),))

    audiomode = models.CharField(
        choices=_AUDIO_CHOICES,
        max_length=30
    )

    repeatscount = models.IntegerField(
        validators=(
            MinValueValidator(1),
        )
    )

    createdon = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name
