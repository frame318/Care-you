from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('liff', views.liff, name='liff'),
    path('st5', views.st5, name='st5'),
    path('q8', views.q8, name='q8'),
    path('q9', views.q9, name='q9'),
    path('reminder', views.reminder, name='reminder'),
    path('reminder-add/<str:userid>', views.reminder_add, name='reminder_add'),
    path('reminder-add', views.reminder_add, name='reminder_add'),
    path('reminder-delete/<str:userid>/<str:id>', views.reminder_delete, name='reminder_delete'),
    path('reminder-delete/<str:id>', views.reminder_delete, name='reminder_delete'),
    path('reminder-edit/<str:id>', views.reminder_edit, name='reminder_edit'),
    path('reminder/<str:userid>', views.reminder, name='reminder'),
    path('reminderdrug', views.reminderdrug, name='reminderdrug'),
    path('reminderdrug/<str:userid>', views.reminderdrug, name='reminderdrug'),
]
