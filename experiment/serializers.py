from rest_framework import serializers
from experiment.models import Experiment
from experiment_session.serializers import ExperimentSessionSerializer
from experiment_preset.serializers import ExperimentPresetSerializer


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Experiment
        fields = ('id', 'name', 'settings', 'createdon', 'status', 'sessions', 'startedon', 'finishedon',)
        read_only = ('createdon', 'sessions', 'status', 'startedon', 'finishedon')
        include = {
            'sessions': ExperimentSessionSerializer(),
            'settings': ExperimentPresetSerializer()
        }
