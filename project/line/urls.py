from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.callback, name='callback'),
    path('webhook', views.webhook, name='webhook'),
]
