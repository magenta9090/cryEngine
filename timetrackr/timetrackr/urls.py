from django.conf.urls import patterns, include, url
from django.contrib import admin
import timetrackr.views as ttv

urlpatterns = patterns(
    '',
    url(r'accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'admin/login.html'}),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^timetrackr/$', ttv.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
