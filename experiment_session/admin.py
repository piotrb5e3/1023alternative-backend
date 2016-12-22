from django.contrib import admin
from experiment_session.models import ExperimentSession, Combination, Repeat

# Register your models here.
admin.site.register(ExperimentSession)
admin.site.register(Combination)
admin.site.register(Repeat)
