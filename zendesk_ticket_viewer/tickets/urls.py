from django.urls import path
from .import views

app_name = "tickets"

urlpatterns = [
    path('',views.get_tickets,name = 'get_tickets'),
    path('ticket_detail/<int:ticket_id>',views.get_ticket_details,name = 'get_ticket_details')
]