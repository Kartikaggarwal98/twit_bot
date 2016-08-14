from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pokemon','search.views.index',name='index'),
    #url(r'^pokemon','search.views.random',name='random'),
    url(r'^search$','search.views.srch',name='search'),  # search- folder name, views- file name, srch- function in views.py
    url(r'^search/(\d+)','search.views.srch2',name='search2'), #regex - unnamed grouping (\d+) 
    #url(r'^search/(?P<foo>\d+)','search.views.srch3',name='search2'),

)
