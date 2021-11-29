from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch



class TestViews(TestCase):
    
    def test_get_tickets(self):
        client = Client()
        response = client.get(reverse('tickets:gt_tkts'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'main/tickets.html')


    def test_get_ticket_details(self):
        client = Client()
        response = client.get(reverse('tickets:gt_tkt_dtls', args=[1]))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'main/ticket_detail.html')
