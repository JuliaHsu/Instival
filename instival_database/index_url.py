from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^$',views.showHomePage),
  url(r'^login',views.showLogin),
  url(r'^profile',views.showPersonal),
  url(r'^calendar',views.showCalendar),
  url(r'^festival/(?P<pk>\w+)/$', views.festival_each_post_gallery),
  url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail),
  
  url(r'^(?P<name>\w+)/(?P<pk>[0-9]+)/$',views.country_each_festival_album),
  
 )