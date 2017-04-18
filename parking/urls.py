from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^spots/$', views.SpotList.as_view(), name='list'),
    url(r'^spots/latitude=(?P<latitude>[0-9]+)&longitude=(?P<longitude>[0-9]+)&r=(?P<r>[0-9]+)$', views.SpotLatLog.as_view()),
    url(r'^parked/$', views.ParkedList.as_view(), name='parked'),
    url(r'^reserved/$',views.ReserveIT.as_view(),name="reserved"),
]
