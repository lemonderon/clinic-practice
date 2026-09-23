from django.db import migrations


DEMO_RECORDS = (
    (
        "ClinicInfo",
        {"pk": 1},
        {
            "name": (
                "Northstar Veterinary Clinic",
                "Ветеринарна клініка «Північна зірка»",
            ),
            "description": (
                "Compassionate veterinary care for pets at every stage of life.\n"
                "Visit our team for preventive care, treatment, and practical support.",
                "Дбайлива ветеринарна допомога домашнім улюбленцям на кожному "
                "етапі життя.\nЗвертайтеся до нашої команди для профілактики, "
                "лікування та практичної підтримки.",
            ),
            "contacts": (
                "Phone: (555) 010-2040\nEmail: hello@northstar-vet.example",
                "Електронна пошта: hello@northstar-vet.example",
            ),
        },
    ),
    (
        "Branch",
        {"pk": 1},
        {
            "name": (
                "Riverside Veterinary Branch",
                "Ветеринарна філія «Набережна»",
            ),
            "manager_name": ("Maya Chen", "Марія Коваленко"),
        },
    ),
    (
        "Branch",
        {"pk": 2},
        {
            "name": (
                "Harborview Veterinary Branch",
                "Ветеринарна філія «Портова»",
            ),
            "manager_name": ("Daniel Okafor", "Данило Бондаренко"),
        },
    ),
    (
        "Service",
        {"pk": 1, "code": "VET-101"},
        {
            "name": (
                "Puppy Wellness and Preventive Care",
                "Профілактичний огляд і догляд за цуценятами",
            ),
            "description": (
                "This welcoming preventive-care visit helps new puppy families "
                "establish healthy routines from the first months at home. The "
                "veterinary team reviews vaccinations, parasite prevention, "
                "nutrition, dental habits, and safe socialization while answering "
                "practical questions about sleep, exercise, and common household "
                "hazards. Families leave with a tailored care calendar, clear "
                "warning signs to watch for, and a calm plan for introducing future "
                "visits without unnecessary stress for their puppy.",
                "Цей дружній профілактичний прийом допомагає родинам, у яких "
                "з’явилося цуценя, сформувати здорові звички з перших місяців удома. "
                "Ветеринарна команда розглядає вакцинацію, профілактику паразитів, "
                "харчування, догляд за зубами та безпечну соціалізацію, а також "
                "відповідає на практичні запитання про сон, фізичну активність і "
                "поширені побутові небезпеки. Після візиту родина отримує "
                "індивідуальний календар догляду, перелік тривожних ознак і спокійний "
                "план підготовки до наступних відвідувань без зайвого стресу для "
                "цуценяти.",
            ),
            "coordinator_name": ("Aisha Patel", "Аліна Петренко"),
            "preparation": (
                "Bring vaccination records and a list of current foods or "
                "supplements.\nUse a secure carrier or leash for the journey.",
                "Візьміть із собою записи про вакцинацію та список кормів і добавок, "
                "які зараз отримує цуценя.\nДля поїздки використовуйте надійну "
                "переноску або повідець.",
            ),
        },
    ),
    (
        "Service",
        {"pk": 2, "code": "VET-204"},
        {
            "name": (
                "Calm Coat and Mobility Clinic",
                "Консультація щодо здоров’я шкіри та рухливості",
            ),
            "description": (
                "A gentle appointment for pets who need support with skin comfort, "
                "movement, or both.",
                "Дбайливий прийом для тварин, яким потрібна допомога через дискомфорт "
                "шкіри, обмежену рухливість або обидва стани.",
            ),
            "coordinator_name": ("Jon Bell", "Юрій Мельник"),
            "preparation": (
                "Bring a short list of recent symptoms and any medicines.",
                "Підготуйте короткий список нещодавніх симптомів і всіх ліків, які "
                "отримує тварина.",
            ),
        },
    ),
    (
        "Service",
        {"pk": 3, "code": "VET-310"},
        {
            "name": (
                "Senior Pet Dental Review",
                "Стоматологічний огляд для літніх тварин",
            ),
            "description": (
                "A focused dental assessment for older pets, with prevention advice "
                "and treatment planning.",
                "Цілеспрямований стоматологічний огляд для літніх тварин із порадами "
                "щодо профілактики та плануванням лікування.",
            ),
            "coordinator_name": ("Elena Ruiz", "Олена Романюк"),
            "preparation": (
                "Bring your pet's medication list and avoid feeding for two hours "
                "before the visit unless the care team advises otherwise.",
                "Візьміть із собою список ліків, які отримує тварина, і не годуйте її "
                "протягом двох годин перед візитом, якщо команда клініки не порадила "
                "іншого.",
            ),
        },
    ),
)


def _update_unchanged_demo_fields(apps, schema_editor, reverse):
    database_alias = schema_editor.connection.alias

    for model_name, lookup, field_translations in DEMO_RECORDS:
        model = apps.get_model("clinic", model_name)
        record = model.objects.using(database_alias).filter(**lookup).first()
        if record is None:
            continue

        changed_fields = []
        for field_name, (english_value, ukrainian_value) in field_translations.items():
            source_value, target_value = (
                (ukrainian_value, english_value)
                if reverse
                else (english_value, ukrainian_value)
            )
            if getattr(record, field_name) != source_value:
                continue
            setattr(record, field_name, target_value)
            changed_fields.append(field_name)

        if changed_fields:
            record.save(using=database_alias, update_fields=changed_fields)


def localize_demo_data(apps, schema_editor):
    _update_unchanged_demo_fields(apps, schema_editor, reverse=False)


def restore_english_demo_data(apps, schema_editor):
    _update_unchanged_demo_fields(apps, schema_editor, reverse=True)


class Migration(migrations.Migration):
    dependencies = [
        ("clinic", "0003_localize_model_metadata"),
    ]

    operations = [
        migrations.RunPython(localize_demo_data, restore_english_demo_data),
    ]
