from django.contrib import admin
from experiment_session.models import ExperimentSession, Combination

# Register your models here.
admin.site.register(ExperimentSession)
admin.site.register(Combination)
