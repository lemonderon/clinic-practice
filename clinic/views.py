from django.shortcuts import render

from .models import Service


def service_list(request):
    services = Service.objects.select_related("branch").all()
    return render(request, "clinic/service_list.html", {"services": services})
