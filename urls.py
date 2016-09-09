"""gpgvote URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
import views
import django.views
import gpgauth.views
import polls.views
import captcha

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # Example:
    # (r'^gpgvote/', include('gpgvote.foo.urls')),
    url(r'^site_media/(?P<path>.*)$', serve,
    {'document_root': 'templates/media'}),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$', views.main),
    url(r'^userinfo/(?P<user_id>\d+)/$', views.userinfo),
    url(r'^register/$', gpgauth.views.register),
    url(r'^batch_import/$', gpgauth.views.batch_import),
    url(r'^renew/(?P<username>.*)$', gpgauth.views.renew),
    url(r'^login/$', gpgauth.views.login_view),
    url(r'^logout/$', gpgauth.views.logout_view),
    url(r'^createpoll/$', polls.views.createpoll),
    url(r'^editpoll/(?P<poll_id>\d+)/$', polls.views.editpoll),
    url(r'^add_voters/(?P<poll_id>\d+)/$', polls.views.add_voters),
    url(r'^deletepoll/(?P<poll_id>\d+)/$', polls.views.deletepoll),
    url(r'^mypolls/$', polls.views.mypolls),
    url(r'^voters_list/(?P<poll_id>\d+)/$', polls.views.voters_list),
    url(r'^vote/(?P<poll_id>\d+)/$', polls.views.vote),
    url(r'^results/(?P<poll_id>\d+)/$', polls.views.results),
    url(r'^results/(?P<poll_id>\d+)/votes_list/$', polls.views.votes_list)
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
]
