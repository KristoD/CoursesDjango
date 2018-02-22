from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/course$', views.process),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroy/process$', views.destroy_process),
    url(r'^comment/(?P<id>\d+)/create$', views.comment),
    url(r'^comment/process$', views.comment_process)
]