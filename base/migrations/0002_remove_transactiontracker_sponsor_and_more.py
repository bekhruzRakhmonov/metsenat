# Generated by Django 4.1.1 on 2022-10-01 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transactiontracker",
            name="sponsor",
        ),
        migrations.AddField(
            model_name="transactiontracker",
            name="org_sponsor",
            field=models.ForeignKey(
                default=5,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_org_sponsor",
                to="base.orgapplication",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transactiontracker",
            name="physical_sponsor",
            field=models.ForeignKey(
                default=5,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_physical_sponsor",
                to="base.orgapplication",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Sponsor",
        ),
    ]
