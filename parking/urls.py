from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^spotsavailable/$', views.ListedSpots.as_view(), name='list'),
    url(r'^spotsnearby/latitude=(?P<latitude>[0-9]+)&longitude=(?P<longitude>[0-9]+)&r=(?P<r>[0-9]+)$', views.SpotinRadius.as_view()),
    url(r'^occupiedspots/$', views.OccupiedSpots.as_view(), name='parked'),
    url(r'^reservedspots/$',views.ReservedSpot.as_view(),name="reserved"),
]
