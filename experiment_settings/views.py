from rest_framework import viewsets, permissions
from experiment_settings.models import ExperimentSettings
from experiment_settings.serializers import ExperimentSettingsSerializer


class ExperimentSettingsViewSet(viewsets.ModelViewSet):
    queryset = ExperimentSettings.objects.all()
    serializer_class = ExperimentSettingsSerializer
    permission_classes = (permissions.AllowAny,)
