from rest_framework import serializers
from experiment.models import Experiment
from experiment_session.serializers import ExperimentSessionSerializer


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Experiment
        fields = ('id', 'name', 'lightoffmode', 'lightofftimeout', 'audiomode', 'repeatscount',
                  'sessions',)
        include = {
            'sessions': ExperimentSessionSerializer()
        }
