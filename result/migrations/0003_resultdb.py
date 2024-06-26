# Generated by Django 5.0.2 on 2024-04-01 05:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_account_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.IntegerField(default=0)),
                ('bengali', models.IntegerField(default=0)),
                ('mathematics', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('programming', models.IntegerField(default=0)),
                ('environment', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
