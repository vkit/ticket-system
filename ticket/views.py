from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View, DetailView
from .models import Ticket, TicketComment
from .forms import TicketForm, TicketCommentForm, TicketUpdateForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
import datetime
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin


class TicketView(LoginRequiredMixin, ListView):
    template_name = 'ticket_list.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(TicketView, self).get_context_data(**kwargs)
        context['form'] = TicketForm()
        context['pending_count'] = Ticket.objects.filter(
            status='PENDING').count()
        context['solved_count'] = Ticket.objects.filter(
            status='SOLVED').count()
        context['closed_count'] = Ticket.objects.filter(
            status='CLOSED').count()
        context['total_ticket'] = Ticket.objects.count()
        context['posts'] = Ticket.objects.filter(
            created_by=self.request.user).order_by('-created')
        context['user'] = self.request.user
        context['date'] = datetime.datetime.now()
        print "I am heretoo"
        return context

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.instance
            instance.created_by = self.request.user
            instance.save()
            print 'i m valid form'
            form.save()
            messages.success(
                request, 'Well done!Your Ticket is Addded Succesfully.')
        else:
            print form.errors
        return HttpResponseRedirect('/ticket/list/')


class TicketDetailView(DetailView):
    template_name = 'ticket_detail.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context['form'] = TicketCommentForm()
        context['post'] = Ticket.objects.get(pk=self.kwargs.get('pk'))
        context['form1'] = TicketUpdateForm(instance=context['post'])
        return context


class TicketCommentView(View):

    def post(self, request, *args, **kwargs):
        form = TicketCommentForm(request.POST)
        if form.is_valid():
            instance = form.instance
            post = Ticket.objects.get(pk=self.kwargs.get('pk'))
            instance.post = post
            form.save()
            messages.success(
                request, 'Well done!Your Comment is Added Succesfully.')
        else:
            print form.errors
        return HttpResponseRedirect(
            '/ticket/{0}/detail/'.format(self.kwargs.get('pk')))


class TicketupdateView(View):

    def post(self, request, *args, **kwargs):
        post = Ticket.objects.get(pk=self.kwargs.get('pk'))
        form1 = TicketUpdateForm(request.POST, instance=post)
        if form1.is_valid():
            print 'I am form1 valid'
            form1.save()
            messages.success(
                request, 'Well done!Your status is updated succesfully.')
        else:
            print form1.errors
        return HttpResponseRedirect(
            '/ticket/{0}/detail/'.format(post.id))


class PendingStatusView(ListView):
    template_name = 'pending.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(PendingStatusView, self).get_context_data(**kwargs)
        context['count'] = Ticket.objects.filter(status='PENDING').count()
        context['pending_tickets'] = Ticket.objects.filter(status='PENDING')
        return context


class SolvedStatusView(ListView):
    template_name = 'solved.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(SolvedStatusView, self).get_context_data(**kwargs)
        context['count'] = Ticket.objects.filter(status='SOLVED').count()
        context['solved_tickets'] = Ticket.objects.filter(status='SOLVED')
        return context


class ClosedStatusView(ListView):
    template_name = 'closed.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(ClosedStatusView, self).get_context_data(**kwargs)
        context['count'] = Ticket.objects.filter(status='CLOSED').count()
        context['closed_tickets'] = Ticket.objects.filter(status='CLOSED')
        return context


class TotalStatusView(ListView):
    template_name = 'total.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(SolvedStatusView, self).get_context_data(**kwargs)
        context['count'] = Ticket.objects.filter(status='SOLVED').count()
        context['solved_tickets'] = Ticket.objects.filter(status='SOLVED')
        return context


import pdfcrowd
from django.http import HttpResponse

class GenerateView(View):

    def post(self, request, *args, **kwargs):
        # create an API client instance
        client = pdfcrowd.Client("username", "apikey")

        # convert a web page and store the generated PDF to a variable
        pdf = client.convertFile("/home/raghu/ticketing/ticket/templates/hello.html")

        response = HttpResponse(mimetype="application/pdf")
        response["Cache-Control"] = "max-age=0"
        response["Accept-Ranges"] = "none"
        response["Content-Disposition"] = "attachment; filename=google_com.pdf"

        response.write(pdf)

        response = HttpResponse(mimetype="text/plain")
        return response


class TestingView(LoginRequiredMixin, generic.ListView):
    template_name = 'testing.html'
    
    def get(self, request):
        model = TicketComment.objects.get(name='fd')
        serialized_obj = serializers.serialize('json', [ model, ])
        return render(request, 'testing.html' ,{'foo':serialized_obj})

        
