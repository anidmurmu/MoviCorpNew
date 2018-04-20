from django.contrib import admin
from django.urls import path, include
from ticket import views

app_name = 'ticket'

urlpatterns = [
    path('', views.all_tickets, name='all_tickets'),
    path('login/', views.login_view, name='login'),
    path('list/', views.list_view, name='list'),
    path('info/', views.info_view, name='info'),
    path('addticket/', views.add_ticket_view, name='add_ticket'),
]
