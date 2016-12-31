import random
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from experiment_session.models import ExperimentSession, Repeat, Combination, STATUS_FINISHED, STATUS_IN_PROGRESS
from experiment_session.serializers import ExperimentSessionSerializer

from common.views import get_session


class ExperimentSessionViewSet(viewsets.ModelViewSet):
    queryset = ExperimentSession.objects.all()
    serializer_class = ExperimentSessionSerializer
    permission_classes = (permissions.AllowAny,)


@api_view()
def get_experiment_settings(request):
    session = get_session(request)
    return Response({
        'sessionId': session.id,
        'audiomode': session.experiment.audiomode,
        'lightoffmode': session.experiment.lightoffmode,
        'lightofftimeout': session.experiment.lightofftimeout,
        'askUserData': False if session.userage else True,
        'runTrainingSession': session.showtraining,
    })


@api_view()
def get_lightset(request):
    try:
        session = get_session(request)
        current_repeat = session.get_or_create_current_repeat()
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    if current_repeat.combinations.filter(status=STATUS_IN_PROGRESS).count() > 0:
        return Response('Another combination is in progress', status=status.HTTP_400_BAD_REQUEST)
    lightsets = set([i for i in range(1, 1024)])
    used_lightsets = current_repeat.combinations.all()
    for l in used_lightsets:
        lightsets.discard(l.lightset)
    lightset = random.choice(list(lightsets))
    Combination.objects.create(repeat=current_repeat, lightset=lightset)
    return Response(lightset)


@api_view()
def pause_current_lightset(request):
    try:
        session = get_session(request)
        current_repeat = session.get_or_create_current_repeat()
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    current_lightset = current_repeat.combinations.filter(status=STATUS_IN_PROGRESS).first()

    if not current_lightset:
        return Response('No lightset to pause', status=status.HTTP_400_BAD_REQUEST)

    current_lightset.delete()

    return Response('OK')
