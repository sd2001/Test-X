# Generated by Django 3.1.7 on 2021-03-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practioners', '0002_available_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='end2',
        ),
        migrations.RemoveField(
            model_name='available',
            name='start2',
        ),
        migrations.AlterField(
            model_name='available',
            name='end1',
            field=models.TimeField(verbose_name='End(hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='available',
            name='start1',
            field=models.TimeField(verbose_name='Start(hh:mm:ss)'),
        ),
    ]
