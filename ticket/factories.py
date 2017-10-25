from factory.django import DjangoModelFactory
from ticket.models import Ticket
from django.contrib.auth.models import User
import factory
# from django.utils import timezone


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username%d" % n)
    password = 'greendisgn123'
    email = 'rao.raghavendra41@gmail.com'


class TicketFactory(DjangoModelFactory):
    class Meta:
        model = Ticket

    title = 'green design'
    created_by = factory.SubFactory(UserFactory)
    ticket_id = 014
    body = 'some body'
    choice = 'CLOSED'
    file = factory.django.FileField(filename='/home/raghu/Desktop/raghu.jpg')
