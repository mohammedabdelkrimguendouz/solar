# Generated by Django 5.2.4 on 2025-07-09 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('number_of_panels', models.IntegerField(default=0)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
