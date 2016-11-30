from rest_framework import viewsets, permissions
from experiment.models import  Experiment
from experiment.serializers import ExperimentSerializer


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.AllowAny,)

