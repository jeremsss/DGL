from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'dglsys'

urlpatterns = [
    path('',views.MainPage, name="MainPage"),
    path('Information/',views.Information, name="Information"),
    path('records/',views.records, name="records"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('update1/<int:id>', views.update1, name='update1'),
]