from django.db import models
from experiment_preset.models import ExperimentPreset
from experiment_session.models import ExperimentSession


class Experiment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_ACTIVE = 'active'
    STATUS_FINISHED = 'finished'
    STATUS_ARCHIVED = 'archived'
    _STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACTIVE, 'Finished'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_ARCHIVED, 'Archived')
    )

    def initial_sessions_left(self):
        return self.settings.repeatsCount

    name = models.CharField(max_length=255, unique=True)
    settings = models.ForeignKey(ExperimentPreset, on_delete=models.PROTECT, null=False)
    createdon = models.DateTimeField(auto_now_add=True, editable=False)
    startedon = models.DateTimeField(blank=True, null=True)
    finishedon = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=_STATUS_CHOICES, default=STATUS_PENDING)

    @property
    def sessions_done(self):
        return (ExperimentSession
                .objects
                .filter(experiment=self, status=ExperimentSession.STATUS_FINISHED)
                .count())

    @property
    def progress(self):
        return self.sessions_done / self.settings.repeatsCount

    def __str__(self):
        return self.name
