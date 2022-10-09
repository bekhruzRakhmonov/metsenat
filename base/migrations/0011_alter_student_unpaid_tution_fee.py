# Generated by Django 4.1.1 on 2022-10-03 16:37

import base.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_alter_student_unpaid_tution_fee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="unpaid_tution_fee",
            field=models.FloatField(
                validators=[base.validators.payment_amount_validator],
                verbose_name="Unpaid Tution fee",
            ),
        ),
    ]
