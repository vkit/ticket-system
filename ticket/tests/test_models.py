from django.test import TestCase
from ticket.models import Ticket
from ticket.factories import TicketFactory


class TicketTest(TestCase):
    def setUp(self):
        self.ticket = TicketFactory.create()

    def test_ticket(self):
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertTrue(isinstance(self.ticket, Ticket))
