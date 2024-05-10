from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from services.forms import ServiceForm
from services.models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'


class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('services:service_list')


class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_update.html'
    success_url = reverse_lazy('services:service_list')

