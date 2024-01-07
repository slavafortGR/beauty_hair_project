# Generated by Django 5.0 on 2024-01-07 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=1)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=160)),
                ('kind', models.IntegerField()),
                ('primary', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
    ]
