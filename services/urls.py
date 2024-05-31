from django.contrib import admin
from django.urls import path
from .views import CreateServiceView, DeleteServiceView, ServiceListView

app_name = 'services'

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),
    path("create/", CreateServiceView.as_view(), name="create"),
    path("delete/<int:pk>/", DeleteServiceView.as_view(), name="delete"),
]