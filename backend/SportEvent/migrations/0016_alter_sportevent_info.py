# Generated by Django 4.2.7 on 2023-12-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportEvent', '0015_alter_sportevent_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportevent',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
