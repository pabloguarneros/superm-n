# Generated by Django 3.2 on 2021-05-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_entry_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
