from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheWagon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'HomePage.views.home'),
	url(r'^contact/$', 'HomePage.views.contact'), 
	url(r'^about/$', 'HomePage.views.about'),
	url(r'^login/$', 'HomePage.views.login'),
	url(r'^signup/$', 'HomePage.views.signup'),
	url(r'^postad/$', 'HomePage.views.postad'),
)
