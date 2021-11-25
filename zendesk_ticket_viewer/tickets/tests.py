from django.test import TestCase

# Create your tests here.
class TestCases(TestCase):

    def test_get_tickets_url(self):
        url = 'https://127.0.0.1:/'
        response = self.client.get(url)
        status_code = response.status_code
        self.assertIsNotNone(response)
        self.assertEqual(status_code,200)

    def test_get_ticket_details(self):
        url = 'https://127.0.0.1:/ticket_detail/1'
        response = self.client.get(url)
        status_code = response.status_code
        self.assertIsNotNone(response)
        self.assertEqual(status_code,200)