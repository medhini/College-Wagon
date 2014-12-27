from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'market.views.home'),
	url(r'^contact/$', 'market.views.contact'), 
	url(r'^about/$', 'market.views.about'),
	url(r'^login/$', 'market.views.login'),
	url(r'^signup/$', 'market.views.signup'),
	url(r'^postad/$', 'market.views.postad'),
   	# url(r'^admin/', include(admin.site.urls)),
)
