import csv
from io import StringIO
from slugify import slugify
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from experiment.models import Experiment
from experiment.serializers import ExperimentSerializer


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.AllowAny,)


@csrf_exempt
def generate_unused_list_view(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    if 'experiment_id' not in request.POST:
        return HttpResponse(status=400)

    experiment = get_object_or_404(Experiment, id=request.POST['experiment_id'])

    response = StreamingHttpResponse(write_csv(experiment), content_type='text/csv')
    filename = 'unused_credentials_' + slugify(experiment.name) + '.txt'
    response['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


def write_csv(experiment):
    for session in experiment.sessions.all():
        if session.is_unused():
            yield "Identifier: {:<30} Password: {:<30}\n\n".format(session.userid, session.userpass)


def csv_from_list(row):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(row)
    output.seek(0)
    return output.read()
