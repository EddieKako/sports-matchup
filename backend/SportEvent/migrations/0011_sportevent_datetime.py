# Generated by Django 4.2.7 on 2023-12-03 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SportEvent', '0010_remove_sportevent_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportevent',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
