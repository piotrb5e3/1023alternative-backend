from experiment import urls as experiment_urls
from experiment_session import urls as experiment_session_urls
from experiment_event import urls as experiment_event_urls
from experiment_report import urls as experiment_report_urls

urlpatterns = (experiment_urls.urlpatterns
               + experiment_session_urls.urlpatterns
               + experiment_event_urls.urlpatterns
               + experiment_report_urls.urlpatterns)
