from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.views import get_session

from experiment_event.models import Event


@api_view()
def report_begin_display(request):
    try:
        session = get_session(request)
        current_lightset = session.get_current_lightset()
        Event.objects.create(combination=current_lightset, eventtype=Event.TYPE_COMBINATION_STARTED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response('OK')


@api_view()
def report_finish_display(request):
    try:
        session = get_session(request)
        current_lightset = session.get_current_lightset()
        Event.objects.create(combination=current_lightset, eventtype=Event.TYPE_COMBINATION_FINISHED)
        current_lightset.finish()
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response('OK')
