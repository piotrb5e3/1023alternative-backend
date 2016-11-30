from django.db import models
from django.core.validators import MinValueValidator


class ExperimentSettings(models.Model):
    TIMEOUT_FIXED = 'fixed'
    TIMEOUT_RESPONSIVE = 'responsive'

    FEEDBACK_NONE = 'none'
    FEEDBACK_NEGATIVE_AUDIO = 'n_audio'

    name = models.CharField(unique=True, max_length=255)

    timeout_mode = models.CharField(
        choices=(
            (TIMEOUT_FIXED, 'Fixed'),
            (TIMEOUT_RESPONSIVE, 'Responsive'),
        ),
        max_length=30
    )

    timeout_value = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

    feedback_mode = models.CharField(
        choices=(
            (FEEDBACK_NONE, 'None'),
            (FEEDBACK_NEGATIVE_AUDIO, 'Audio on error'),
        ),
        max_length=30
    )

    repeats_count = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )

