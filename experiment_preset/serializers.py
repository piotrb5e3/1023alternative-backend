from rest_framework import serializers
from experiment_preset.models import ExperimentPreset


class ExperimentPresetSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ExperimentPreset
        fields = (
            'id',
            'name',
            'timeoutmode',
            'timeoutvalue',
            'feedbackmode',
            'repeatscount',
        )
