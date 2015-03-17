from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.contrib.auth.views import login, logout, password_reset

urlpatterns = [
	url(r'^$', include('home.urls', namespace='home') ),  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logbooks/', include('logbooks.urls', namespace="logbooks")),
    url(r'^accounts/login/$', login),
    url(r'^accounts/password_reset/$', password_reset),
    url(r'^accounts/logout/$', logout ),
]

