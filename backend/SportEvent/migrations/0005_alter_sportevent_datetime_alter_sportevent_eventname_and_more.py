# Generated by Django 4.2.7 on 2023-12-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportEvent', '0004_alter_sportevent_datetime_alter_sportevent_eventname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportevent',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='eventname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='location_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='location_city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='location_state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='location_zip',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='phonenum',
            field=models.CharField(max_length=200),
        ),
    ]
