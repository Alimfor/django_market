from django.urls import path

from services.views import ServiceCreate, ServiceUpdate, ServiceListView, ServiceDetailView

app_name = "services"

urlpatterns = [
    path("new/", ServiceCreate.as_view(), name="service_create"),
    path("edit/<int:pk>/", ServiceUpdate.as_view(), name="service_update"),
    path("list/", ServiceListView.as_view(), name="service_list"),
    path("detail/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
]