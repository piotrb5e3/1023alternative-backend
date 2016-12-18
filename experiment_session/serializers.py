from rest_framework.serializers import ModelSerializer

from experiment_session.models import ExperimentSession, Combination
from experiment_event.serializers import EventSerializer


class CombinationSerializer(ModelSerializer):
    class Meta:
        model = Combination
        fields = ('id', 'session', 'lightset', 'events', 'status')
        include = {
            'events': EventSerializer()
        }


class ExperimentSessionSerializer(ModelSerializer):
    class Meta:
        model = ExperimentSession
        fields = ('id', 'experiment', 'status', 'combinations', 'number', 'progress')
        read_only_fields = ('id', 'progress',)
        include = {
            'combinations': CombinationSerializer()
        }
