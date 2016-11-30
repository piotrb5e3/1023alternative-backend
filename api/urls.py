from experiment import urls as experiment_urls
from experiment_settings import urls as experiment_settings_urls

urlpatterns = experiment_urls.urlpatterns + experiment_settings_urls.urlpatterns
