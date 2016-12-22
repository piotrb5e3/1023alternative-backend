from rest_framework import viewsets, permissions
from experiment_session.models import ExperimentSession
from experiment_session.serializers import ExperimentSessionSerializer


class ExperimentSessionViewSet(viewsets.ModelViewSet):
    queryset = ExperimentSession.objects.all()
    serializer_class = ExperimentSessionSerializer
    permission_classes = (permissions.AllowAny,)
