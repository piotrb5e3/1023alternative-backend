from rest_framework.serializers import ModelSerializer

from experiment_event.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'combination', 'eventtype', 'time',)
