from rest_framework import viewsets, permissions
from experiment_session.models import ExperimentSession, Combination
from experiment_session.serializers import (ExperimentSessionSerializer,
                                            CombinationSerializer)


class ExperimentSessionViewSet(viewsets.ModelViewSet):
    queryset = ExperimentSession.objects.all()
    serializer_class = ExperimentSessionSerializer
    permission_classes = (permissions.AllowAny,)


class CombinationViewSet(viewsets.ModelViewSet):
    queryset = Combination.objects.all()
    serializer_class = CombinationSerializer
    permission_classes = (permissions.AllowAny,)
