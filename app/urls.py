from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]