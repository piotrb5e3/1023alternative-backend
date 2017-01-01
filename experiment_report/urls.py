from django.conf.urls import url
from experiment_report.views import generate_report_view

urlpatterns = [
    url(r'^extra/report', generate_report_view)
]
