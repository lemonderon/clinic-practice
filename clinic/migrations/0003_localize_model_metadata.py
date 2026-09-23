import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinic", "0002_clinicinfo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="branch",
            options={
                "ordering": ["name"],
                "verbose_name": "філія",
                "verbose_name_plural": "філії",
            },
        ),
        migrations.AlterModelOptions(
            name="clinicinfo",
            options={
                "verbose_name": "запис про клініку",
                "verbose_name_plural": "записи про клініку",
            },
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["code"],
                "verbose_name": "послуга",
                "verbose_name_plural": "послуги",
            },
        ),
        migrations.AlterField(
            model_name="branch",
            name="manager_name",
            field=models.CharField(max_length=120, verbose_name="ім’я керівника"),
        ),
        migrations.AlterField(
            model_name="branch",
            name="name",
            field=models.CharField(max_length=120, verbose_name="назва"),
        ),
        migrations.AlterField(
            model_name="clinicinfo",
            name="contacts",
            field=models.TextField(verbose_name="контактна інформація"),
        ),
        migrations.AlterField(
            model_name="clinicinfo",
            name="description",
            field=models.TextField(verbose_name="опис"),
        ),
        migrations.AlterField(
            model_name="clinicinfo",
            name="name",
            field=models.CharField(max_length=160, verbose_name="назва"),
        ),
        migrations.AlterField(
            model_name="service",
            name="branch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="services",
                to="clinic.branch",
                verbose_name="філія",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="code",
            field=models.CharField(max_length=20, unique=True, verbose_name="код"),
        ),
        migrations.AlterField(
            model_name="service",
            name="coordinator_contact",
            field=models.CharField(
                max_length=160,
                verbose_name="контакт координатора",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="coordinator_name",
            field=models.CharField(
                max_length=120,
                verbose_name="ім’я координатора",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="description",
            field=models.TextField(verbose_name="опис"),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(max_length=120, verbose_name="назва"),
        ),
        migrations.AlterField(
            model_name="service",
            name="preparation",
            field=models.TextField(blank=True, verbose_name="підготовка до візиту"),
        ),
    ]
