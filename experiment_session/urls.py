from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_session.views import ExperimentSessionViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'experiment-sessions', ExperimentSessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
