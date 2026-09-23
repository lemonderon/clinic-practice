from django.db import models


class ClinicInfo(models.Model):
    name = models.CharField(max_length=160, verbose_name="назва")
    description = models.TextField(verbose_name="опис")
    contacts = models.TextField(verbose_name="контактна інформація")

    class Meta:
        verbose_name = "запис про клініку"
        verbose_name_plural = "записи про клініку"

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=120, verbose_name="назва")
    manager_name = models.CharField(max_length=120, verbose_name="ім’я керівника")

    class Meta:
        ordering = ["name"]
        verbose_name = "філія"
        verbose_name_plural = "філії"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=120, verbose_name="назва")
    code = models.CharField(max_length=20, unique=True, verbose_name="код")
    description = models.TextField(verbose_name="опис")
    coordinator_name = models.CharField(
        max_length=120,
        verbose_name="ім’я координатора",
    )
    coordinator_contact = models.CharField(
        max_length=160,
        verbose_name="контакт координатора",
    )
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="філія",
    )
    preparation = models.TextField(
        blank=True,
        verbose_name="підготовка до візиту",
    )

    class Meta:
        ordering = ["code"]
        verbose_name = "послуга"
        verbose_name_plural = "послуги"

    def __str__(self):
        return f"{self.code} - {self.name}"
