from django.urls import path

from zoogle.contribs.views import index, ssr, ajax, search, zdocs, zmail

urlpatterns = [
    path('', index, name='index'),
    path('ssr', ssr, name='ssr'),
    path('ajax', ajax, name='ajax'),
    path('search', search, name='search'),
    path('zdocs', zdocs, name='zdocs'),
    path('zmail', zmail, name='zmail'),
]
