# Generated by Django 5.0 on 2024-03-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_contact_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='primary',
            field=models.BooleanField(default=True),
        ),
    ]