from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.models import Client, Letter


def index(request):
    return render(request, 'mailing/index.html')

class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email_client')
    success_url = reverse_lazy('mailing:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email_client')
    success_url = reverse_lazy('mailing:client_list')

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')



class LetterCreateView(CreateView):
    model = Letter
    fields = ('title', 'body')
    success_url = reverse_lazy('mailing:letter_list')

class LetterUpdateView(UpdateView):
    model = Letter
    fields = ('title', 'body')
    success_url = reverse_lazy('mailing:letter_list')

class LetterListView(ListView):
    model = Letter

class LetterDetailView(DetailView):
    model = Letter

class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('mailing:letter_list')