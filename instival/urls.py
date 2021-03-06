"""instival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from instival_database import views


admin.autodiscover();
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',include('instival_database.index_url')),
    url(r'^signup/', views.createAccount),


   
    url(r'^post/(?P<user>\w+)/$',views.post_document),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^getuserid/$', views.getuserid, name='getuserid'),
    url(r'^profile/(?P<user>\w+)/$',views.showPersonal),
    url(r'^setProfile/(?P<user>\w+)/$',views.setProfile_view),
    url(r'^setProfile/(?P<user>\w+)/photo/$',views.upload_personalPhoto),

    url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
    url(r'^getuserid/$', views.getuserid, name='getuserid'),


    url(r'^post/(?P<user>\w+)/$',views.post_document),
    url(r'^login/', views.login),
    url(r'^getuserid/$', views.getuserid, name='getuserid'),
    url(r'^profile/(?P<user>\w+)/$',views.showPersonal),


   
]
