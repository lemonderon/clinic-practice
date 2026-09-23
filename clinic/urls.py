from django.urls import path

from . import views

app_name = "clinic"

urlpatterns = [
    path("", views.service_list, name="service-list"),
]
