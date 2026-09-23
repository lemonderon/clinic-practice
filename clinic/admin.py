from django.contrib import admin

from .models import Branch, ClinicInfo, Service

admin.site.site_header = "Адміністрування ветеринарної клініки «Північна зірка»"
admin.site.site_title = "Адмінпанель «Північна зірка»"
admin.site.index_title = "Керування клінікою"


@admin.register(ClinicInfo)
class ClinicInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contacts")
    ordering = ("id",)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "description", "contacts"),
                "description": (
                    "На головній сторінці відображається запис з інформацією "
                    "про клініку з найменшим ідентифікатором."
                ),
            },
        ),
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "manager_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "coordinator_name",
        "coordinator_contact",
        "branch",
    )
