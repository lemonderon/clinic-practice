from django.urls import path

from . import views

app_name = "clinic"

urlpatterns = [
    path("", views.service_list, name="service-list"),
    path("<int:pk>/", views.service_detail, name="service-detail"),
]
