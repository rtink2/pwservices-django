from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Event, Contact
from .forms import EventForm, ContactForm

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/about.html')

class Services(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/services.html')

class Process(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/process.html')

class Consult(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/consult.html')

class Resources(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pw/resources.html')

class EventCreate(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.all().order_by('event_date')
        form = EventForm()

        context = {
            'event': event,
            'form': form,
        }
        return render(request, 'pw/event_create.html', context)


    def post(self, request, *args, **kwargs):
        event = Event.objects.all()
        form = EventForm(request.POST)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.save()
            form = EventForm()

        context = {
            'event': event,
            'form': form,
        }
        return render(request, 'pw/event_create.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class EventListView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.all().order_by('event_date')

        context = {
            'event_list': event,
        }
        return render(request, 'pw/event_list.html', context)

class EventDetailView(DetailView):
    model = Event

class EventEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'body', 'event_date', 'street', 'city', 'state', 'zip_code']
    template_name = 'pw/event_edit.html'

    def get_successUrl(self):
        pk = self.kwargs['pk']
        return reverse_lazy('event_detail', kwargs={'pk': pk})
    
    def test_func(self):
        event = self.get_object()
        return self.request.user.groups.filter(name='Staff').exists()

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'pw/event_delete.html'
    success_url = reverse_lazy('event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user.groups.filter(name='Staff').exists()

class ContactView(View):
    def get(self, request, *args, **kwargs):
        contact = Contact.objects.all()
        form = ContactForm()

        context = {
            'contact': contact,
            'form': form,
        }

        return render(request, 'pw/contact.html', context)
    
    def post(self, request, *args, **kwargs):
        contact = Contact.objects.all()
        form = ContactForm(request.POST)

        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.save()
            form = ContactForm()

        context = {
            'contact': contact,
            'form': form,
        }

        return render(request, 'pw/contact.html', context)
