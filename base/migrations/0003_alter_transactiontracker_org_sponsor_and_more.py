# Generated by Django 4.1.1 on 2022-10-01 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_remove_transactiontracker_sponsor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactiontracker",
            name="org_sponsor",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_org_sponsor",
                to="base.orgapplication",
            ),
        ),
        migrations.AlterField(
            model_name="transactiontracker",
            name="physical_sponsor",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_physical_sponsor",
                to="base.physicalapplication",
            ),
        ),
    ]
