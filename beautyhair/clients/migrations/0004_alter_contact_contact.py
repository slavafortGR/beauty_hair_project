# Generated by Django 5.0 on 2024-02-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_rename_value_contact_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=160, unique=True),
        ),
    ]
