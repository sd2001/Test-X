# Generated by Django 3.1.7 on 2021-03-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateParticipant',
            new_name='CreatePractioner',
        ),
    ]