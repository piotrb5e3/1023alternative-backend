from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_settings.views import ExperimentSettingsViewSet

router = DefaultRouter()
router.register(r'presets', ExperimentSettingsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
