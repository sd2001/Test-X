# Generated by Django 3.1.7 on 2021-03-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practioners', '0010_auto_20210309_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='available',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]