from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_session.views import ExperimentSessionViewSet, get_experiment_settings

router = DefaultRouter(trailing_slash=False)
router.register(r'experiment-sessions', ExperimentSessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^extra/get-experiment', get_experiment_settings),
]
