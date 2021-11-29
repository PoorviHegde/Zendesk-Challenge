from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from tickets.views import get_tickets,get_ticket_details



class TestUrls(SimpleTestCase):
    def test_get_tickets(self):
        url = reverse('tickets:gt_tkts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_tickets)

    def test_get_ticket_details(self):
        url = reverse('tickets:gt_tkt_dtls', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_ticket_details)