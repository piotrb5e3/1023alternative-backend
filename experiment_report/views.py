import csv

from io import StringIO
from slugify import slugify
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from experiment_session.models import ExperimentSession


@csrf_exempt
def generate_report_view(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    if 'session_id' not in request.POST:
        return HttpResponse(status=400)

    session = get_object_or_404(ExperimentSession, id=request.POST['session_id'])

    response = StreamingHttpResponse(write_csv(session), content_type='text/csv')
    filename = 'report_' + slugify(session.experiment.name) + '_' + session.userid + '.csv'
    response['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


def write_csv(session):
    yield from write_experiment_csv(session)
    yield '\n'
    yield from write_events_csv(session)


def write_experiment_csv(session):
    experiment_header = ['name', 'light_off_mode', 'light_off_timeout', 'audio_mode',
                         'repeats_count', 'created_on']
    experiment = session.experiment

    yield csv_from_list(experiment_header)
    yield csv_from_list([experiment.name, experiment.lightoffmode, experiment.lightofftimeout,
                         experiment.audiomode, experiment.repeatscount, experiment.createdon])


def write_events_csv(session):
    event_header = ['repeat_number', 'lightset', 'event_type', 'event_time']
    yield csv_from_list(event_header)

    for repeat in session.repeats.all():
        for combination in repeat.combinations.all():
            for event in combination.events.all():
                yield csv_from_list([repeat.number, combination.lightset, event.eventtype, event.time])


def csv_from_list(row):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(row)
    output.seek(0)
    return output.read()
