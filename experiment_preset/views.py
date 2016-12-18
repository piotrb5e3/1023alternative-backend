from rest_framework import viewsets, permissions
from experiment_preset.models import ExperimentPreset
from experiment_preset.serializers import ExperimentPresetSerializer


class ExperimentPresetViewSet(viewsets.ModelViewSet):
    queryset = ExperimentPreset.objects.all()
    serializer_class = ExperimentPresetSerializer
    permission_classes = (permissions.AllowAny,)
