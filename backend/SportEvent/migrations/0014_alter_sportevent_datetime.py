# Generated by Django 4.2.7 on 2023-12-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportEvent', '0013_alter_sportevent_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportevent',
            name='datetime',
            field=models.DateTimeField(default=''),
        ),
    ]
