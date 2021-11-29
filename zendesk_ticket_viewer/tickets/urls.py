from django.urls import path
from .import views

app_name = "tickets"

urlpatterns = [
    path('', views.get_tickets, name= 'gt_tkts'),
    path('ticket_detail/<int:ticket_id>',views.get_ticket_details, name= 'gt_tkt_dtls')
]