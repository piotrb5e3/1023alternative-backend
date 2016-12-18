from rest_framework import serializers
from experiment.models import Experiment
from experiment_session.serializers import ExperimentSessionSerializer


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Experiment
        fields = ('id', 'name', 'settings', 'createdon', 'status', 'sessions')
        read_only = ('createdon', 'sessions',)
        include = {
            'sessions': ExperimentSessionSerializer()
        }
