from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service


# Create your views here.
class CreateServiceView(LoginRequiredMixin, CreateView):
    model = Service
    fields = ["title", "description", "image"]
    success_url = "/services"


class DeleteServiceView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = "/services"


class ServiceListView(ListView):
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"
    ordering = ["title"]