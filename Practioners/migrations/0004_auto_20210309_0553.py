# Generated by Django 3.1.7 on 2021-03-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practioners', '0003_auto_20210309_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available',
            name='end1',
            field=models.TimeField(blank=True, null=True, verbose_name='End(hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='available',
            name='start1',
            field=models.TimeField(blank=True, null=True, verbose_name='Start(hh:mm:ss)'),
        ),
    ]
