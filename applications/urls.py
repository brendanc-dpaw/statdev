from django.conf.urls import url
from applications import views


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home_page'),
    url(r'^applications/$', views.ApplicationList.as_view(), name='application_list'),
    url(r'^applications/create/$', views.ApplicationCreate.as_view(), name='application_create'),
    url(r'^applications/(?P<pk>\d+)/$', views.ApplicationDetail.as_view(), name='application_detail'),
    url(r'^tasks/(?P<pk>\d+)/reassign/$', views.TaskReassign.as_view(), name='task_reassign'),
]