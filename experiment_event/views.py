from rest_framework import viewsets, permissions
from experiment_event.models import Event
from experiment_event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)
