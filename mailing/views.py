from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.models import Client


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
    def get_success_url(self):
        return reverse('mailing:client_list', args=[self.kwargs.get('pk')])

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
