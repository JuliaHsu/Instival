from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.festival_each_post_gallery),
  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
  url(r'^post/(?P<pk>[0-9]+)/$', views.add_comment_to_post, name='add_comment_to_post'),
  # url(r'^new/$', views.upload),
 )