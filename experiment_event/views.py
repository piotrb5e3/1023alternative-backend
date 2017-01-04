from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.views import get_session

from experiment_event.models import Event

from experiment_session.models import STATUS_IN_PROGRESS

numberToCode = {i: 'bp' + str(i) for i in range(1, 11)}
numberToCode[-1] = 'ibp'


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
    session.refresh_from_db()
    if session.status == STATUS_IN_PROGRESS:
        return Response('OK')
    else:
        return Response('FIN')


@api_view()
def report_button_press(request):
    try:
        session = get_session(request)
        current_lightset = session.get_current_lightset()
        code = get_event_code_from_request(request)
        Event.objects.create(combination=current_lightset, eventtype=code)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response('OK')


def get_event_code_from_request(request):
    if 'number' not in request.GET:
        raise Exception('Missing "number" field')
    try:
        return numberToCode[int(request.GET['number'])]
    except ValueError:
        raise Exception('"number" must be an integer')
    except KeyError:
        raise Exception('Unknown key number')
