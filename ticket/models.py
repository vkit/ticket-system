from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


CHOICE = (
    ('PENDING', 'PENDING'),
    ('SOLVED', 'SOLVED'),
    ('CLOSED', 'CLOSED')
)


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User)
    ticket_id = models.IntegerField(blank=True)
    body = models.TextField()
    status = models.CharField(
        max_length=40,
        choices=CHOICE, default='PENDING'
    )
    updated = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='documents/%Y/%m/%d')

    def save(self, *args, **kwargs):
        ticket_id = Ticket.objects.count()
        if ticket_id == 0:
            self.ticket_id = 1
        else:
            self.ticket_id = ticket_id + 1
        return super(Ticket, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class TicketComment(models.Model):

    post = models.ForeignKey(Ticket, null=True, blank=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        def __str__(self):
            return self.name
