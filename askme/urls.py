from django.urls import path
from django.conf.urls import url, include
from . import views

# urlpatterns = [
#     url(r'^$', views.semantic, name='askme'),
#     url(r'^t/', views.thanks, name='thanks'),
# ]

urlpatterns = [
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]