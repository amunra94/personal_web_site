from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.semantic, name='semantic'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^review/', views.review, name='review'),
]
