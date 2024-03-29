from django.urls import path

from freelance.views import (
    MainPageView
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]