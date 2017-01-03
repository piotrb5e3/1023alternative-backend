from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from experiment_session.utils import random_alphanumeric

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
    userpass = models.CharField(max_length=30)
    showtraining = models.BooleanField(default=True)

    @property
    def progress(self):
        finished = Combination.objects.filter(repeat__session=self, status=STATUS_FINISHED).count()
        return finished / (self.experiment.repeatscount * 1023)

    def get_current_repeat(self):
        repeats_count = self.repeats.count()
        current_repeat = Repeat.objects.filter(session=self, status=STATUS_IN_PROGRESS).first()
        if not current_repeat:
            raise Exception('No currently open reeat')
        return current_repeat

    def get_or_create_current_repeat(self):
        repeats_count = self.repeats.count()
        current_repeat = Repeat.objects.filter(session=self, status=STATUS_IN_PROGRESS).first()
        if not current_repeat:
            if repeats_count >= self.experiment.repeatscount:
                raise Exception('Repeatscount exhausted. Something went wrong!')
            current_repeat = Repeat.objects.create(session=self, number=repeats_count + 1)

        return current_repeat

    def get_current_lightset(self):
        current_repeat = self.get_current_repeat()
        return current_repeat.get_current_lightset()

    def __str__(self):
        return str(self.experiment) + ' (' + self.userid + ')'

    def on_subpart_finish(self):
        if self.repeats.filter(status=STATUS_FINISHED).count() >= self.experiment.repeatscount:
            self.finish()

    def finish(self):
        self.finishedon = datetime.now()
        self.status = STATUS_FINISHED
        self.save()

    @classmethod
    def from_creds(cls, userid, userpass):
        session = cls.objects.filter(userid=userid, userpass=userpass).first()
        if not session:
            raise Exception('No session found')

        if session.status == STATUS_FINISHED:
            raise Exception('Session finished')
        return session

    @classmethod
    def create_new(cls, experiment):
        uid_length = 7
        passwd_length = 8
        userid = random_alphanumeric(length=uid_length)
        counter = 10
        while cls.objects.filter(userid=userid).count() > 0:
            counter -= 1
            if counter <= 0:
                counter = 10
                uid_length += 1
            userid = random_alphanumeric(length=uid_length)

        userpass = random_alphanumeric(length=passwd_length)

        return cls.objects.create(userid=userid, userpass=userpass, experiment=experiment)


class Repeat(models.Model):
    session = models.ForeignKey(ExperimentSession, related_name='repeats', null=False)
    status = models.CharField(max_length=1, default=STATUS_IN_PROGRESS, choices=_STATUS_CHOICES)
    startedon = models.DateTimeField(auto_now_add=True, editable=False)
    finishedon = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField()

    def __str__(self):
        return str(self.session) + '[' + str(self.number) + ']'

    def get_current_lightset(self):
        current_lightset = self.combinations.filter(status=STATUS_IN_PROGRESS).first()
        if not current_lightset:
            raise Exception('No current lightset')
        return current_lightset

    def on_subpart_finish(self):
        if self.combinations.filter(status=STATUS_FINISHED).count() >= 1023:
            self.finish()

    def finish(self):
        self.finishedon = datetime.now()  # suspicious
        self.status = STATUS_FINISHED
        self.save()
        self.session.on_subpart_finish()

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

    def __str__(self):
        return str(self.repeat) + ' : ' + str(self.lightset)

    def finish(self):
        self.status = STATUS_FINISHED
        self.save()
        self.repeat.on_subpart_finish()

    class Meta:
        unique_together = ('repeat', 'lightset')
