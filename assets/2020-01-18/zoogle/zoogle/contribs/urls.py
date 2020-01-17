from django.urls import path

from zoogle.contribs.views import index

urlpatterns = [
    path('', index, name='index'),
]
