from django.db import models


class ClinicInfo(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=120)
    manager_name = models.CharField(max_length=120)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=120)
    coordinator_contact = models.CharField(max_length=160)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="services",
    )
    preparation = models.TextField(blank=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"
