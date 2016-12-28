from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from experiment_session.models import ExperimentSession, STATUS_FINISHED
from experiment_session.serializers import ExperimentSessionSerializer


class ExperimentSessionViewSet(viewsets.ModelViewSet):
    queryset = ExperimentSession.objects.all()
    serializer_class = ExperimentSessionSerializer
    permission_classes = (permissions.AllowAny,)


@api_view()
def get_experiment_settings(request):
    if not ('userid' in request.GET and 'userpass' in request.GET):
        return Response('No credentials supplied', status=status.HTTP_401_UNAUTHORIZED)

    userid = request.GET['userid']
    userpass = request.GET['userpass']
    session = ExperimentSession.objects.filter(userid=userid, userpass=userpass).first()
    if not session:
        return Response('No session found', status=status.HTTP_401_UNAUTHORIZED)

    if session.status == STATUS_FINISHED:
        return Response('Session finished', status=status.HTTP_410_GONE)

    return Response({
        'sessionId': session.id,
        'audiomode': session.experiment.audiomode,
        'lightoffmode': session.experiment.lightoffmode,
        'lightofftimeout': session.experiment.lightofftimeout,
        'askUserData': False if session.userage else True,
        'runTrainingSession': session.showtraining,
    })
