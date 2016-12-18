from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_preset.views import ExperimentPresetViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'experiment-presets', ExperimentPresetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
