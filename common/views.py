from experiment_session.models import ExperimentSession


def get_session(request):
    userid, userpass = creds_from_request(request)
    return ExperimentSession.from_creds(userid, userpass)


def creds_from_request(request):
    if not ('userid' in request.GET and 'userpass' in request.GET):
        raise Exception('No credentials supplied')
    return request.GET['userid'], request.GET['userpass']
