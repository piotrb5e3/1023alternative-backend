from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_session.views import (ExperimentSessionViewSet, get_experiment_settings,
                                      get_lightset, pause_current_lightset, report_user_data,
                                      report_training_finished, create_sessions)

router = DefaultRouter(trailing_slash=False)
router.register(r'experiment-sessions', ExperimentSessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^extra/get-experiment', get_experiment_settings),
    url(r'^extra/get-lightset', get_lightset),
    url(r'^extra/pause-lightset', pause_current_lightset),
    url(r'^extra/report-data', report_user_data),
    url(r'^extra/training-finished', report_training_finished),
    url(r'^extra/create-sessions', create_sessions),
]
