from django.shortcuts import get_object_or_404, render

from .models import Branch, ClinicInfo, Service


def home(request):
    clinic_info = ClinicInfo.objects.order_by("pk").first()
    return render(request, "clinic/home.html", {"clinic_info": clinic_info})


def service_list(request):
    services = Service.objects.select_related("branch").all()
    return render(request, "clinic/service_list.html", {"services": services})


def service_detail(request, pk):
    service = get_object_or_404(
        Service.objects.select_related("branch"),
        pk=pk,
    )
    return render(request, "clinic/service_detail.html", {"service": service})


def branch_detail(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    return render(request, "clinic/branch_detail.html", {"branch": branch})
