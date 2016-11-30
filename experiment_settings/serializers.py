from rest_framework import serializers
from experiment_settings.models import ExperimentSettings


class ExperimentSettingsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ExperimentSettings
        fields = (
            'id',
            'name',
            'timeout_mode',
            'timeout_value',
            'feedback_mode',
            'repeats_count',
        )
