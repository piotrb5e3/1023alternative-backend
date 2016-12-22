from rest_framework.serializers import ModelSerializer

from experiment_session.models import ExperimentSession


class ExperimentSessionSerializer(ModelSerializer):
    class Meta:
        model = ExperimentSession
        fields = ('id', 'experiment', 'status', 'userid', 'username', 'userage', 'usersex',
                  'userpass', 'progress', 'startedon', 'finishedon',)
        read_only_fields = ('progress',)
