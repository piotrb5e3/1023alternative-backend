from django.db import models


class Event(models.Model):
    TYPE_BUTTON_PRESS = 'bp'
    TYPE_COMBINATION_FINISHED = 'fn'
    _TYPE_CHOICES = (
        (TYPE_BUTTON_PRESS, 'Button press'),
        (TYPE_COMBINATION_FINISHED, 'Combination finished'),
    )

    combination = models.ForeignKey('experiment_session.Combination',
                                    related_name='events')
    eventtype = models.CharField(max_length=16, choices=_TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
