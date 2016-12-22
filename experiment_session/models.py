from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS_FINISHED = 'F'
STATUS_IN_PROGRESS = 'P'
_STATUS_CHOICES = (
    (STATUS_FINISHED, "Finished"),
    (STATUS_IN_PROGRESS, "In progress"),
)


class ExperimentSession(models.Model):
    SEX_MALE = 'F'
    SEX_FEMALE = 'M'
    _SEX_CHOICES = (
        (SEX_FEMALE, 'Female'),
        (SEX_MALE, 'Male')
    )

    experiment = models.ForeignKey('experiment.Experiment', related_name='sessions', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    startedon = models.DateTimeField(auto_now_add=True, editable=False)
    finishedon = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(unique=True, max_length=30)
    username = models.CharField(max_length=265, null=True, blank=True)
    userage = models.IntegerField(blank=True, null=True, validators=(MinValueValidator(1),))
    usersex = models.CharField(blank=True, null=True, choices=_SEX_CHOICES, max_length=1)

    @property
    def progress(self):
        return Combination.all.filter(repeat__session=self).count() / (experiment.repeatscount * 1023)

    def __str__(self):
        return str(self.experiment) + ' (' + self.userid + ')'


class Repeat(models.Model):
    session = models.ForeignKey(ExperimentSession, related_name='repeats', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    startedon = models.DateTimeField(auto_now_add=True, editable=False)
    finishedon = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField()

    def __str__(self):
        return str(self.session + '[' + str(number) + ']')

    class Meta:
        unique_together = ('session', 'number')


class Combination(models.Model):
    repeat = models.ForeignKey(Repeat, related_name='combinations', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    lightset = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(1023)
        )
    )
    user = models.CharField(max_length=128)

    def __str__(self):
        return str(self.repeat) + ' : ' + str(self.lightset)

    class Meta:
        unique_together = ('repeat', 'lightset')
