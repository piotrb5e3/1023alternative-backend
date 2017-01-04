from django.db import models


class Event(models.Model):
    TYPE_BUTTON_PRESS_LIST = [('bp' + str(n), 'Button ' + str(n) + ' pressed') for n in range(1, 11)]
    TYPE_INCORRECT_BUTTON_PRESS = 'ibp'
    TYPE_COMBINATION_STARTED = 'st'
    TYPE_COMBINATION_FINISHED = 'fn'
    _TYPE_CHOICES = [
                        (TYPE_COMBINATION_STARTED, 'Combination started'),
                        (TYPE_COMBINATION_FINISHED, 'Combination finished'),
                        (TYPE_INCORRECT_BUTTON_PRESS, 'Incorrect button pressed'),
                    ] + TYPE_BUTTON_PRESS_LIST

    combination = models.ForeignKey('experiment_session.Combination',
                                    related_name='events',
                                    null=False)
    eventtype = models.CharField(max_length=16, choices=_TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.combination) + ' - ' + str(self.eventtype)
