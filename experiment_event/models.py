from django.db import models


class Event(models.Model):
    TYPE_BUTTON_PRESS_MAP = {'bp' + str(n): 'Button ' + str(n) + ' pressed' for n in range(1, 11)}
    TYPE_LEASE = 'ls'
    TYPE_COMBINATION_FINISHED = 'fn'
    _TYPE_CHOICES = [
                        (TYPE_COMBINATION_FINISHED, 'Combination finished'),
                    ] + [(k, v) for k, v in TYPE_BUTTON_PRESS_MAP.items()]

    combination = models.ForeignKey('experiment_session.Combination',
                                    related_name='events',
                                    null=False)
    eventtype = models.CharField(max_length=16, choices=_TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TYPE_BUTTON_PRESS_MAP[self.eventtype]