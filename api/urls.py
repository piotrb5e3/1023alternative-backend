from experiment import urls as experiment_urls
from experiment_session import urls as experiment_session_urls

urlpatterns = (experiment_urls.urlpatterns
               + experiment_session_urls.urlpatterns)
