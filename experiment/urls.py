from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment.views import ExperimentViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'experiments', ExperimentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
