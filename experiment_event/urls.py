from django.conf.urls import url

from experiment_event.views import (report_begin_display, report_finish_display,
                                    report_button_press)

urlpatterns = [
    url(r'^extra/eventbegin', report_begin_display),
    url(r'^extra/eventfinish', report_finish_display),
    url(r'^extra/eventbutton', report_button_press)
]
