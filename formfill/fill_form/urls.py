__author__ = 'Arpit Gang'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fill/', views.form, name='form'),
    url(r'^submit/', views.get_data, name='form'),
]

