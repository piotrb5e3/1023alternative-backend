from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from experiment_event.views import EventViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'events', EventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
