# Generated by Django 5.0.1 on 2024-01-25 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(blank=True, default='shops', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('type', models.CharField(blank=True, choices=[('M', 'Member'), ('A', 'Manager')], default='M', max_length=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Manager', 'Manager')], default='Member', max_length=55)),
                ('start_date', models.DateField()),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.location')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
