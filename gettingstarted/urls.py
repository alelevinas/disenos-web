from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^d1/', hello.views.d1, name='d1'),
    url(r'^d2/', hello.views.d2, name='d2'),
    url(r'^d3/', hello.views.d3, name='d3'),
    url(r'^d4/', hello.views.d4, name='d4')
]
