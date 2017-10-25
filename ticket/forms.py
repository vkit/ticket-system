from django import forms
from .models import Ticket, TicketComment


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'body', 'file')


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ('name', 'email', 'body')


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', ]
