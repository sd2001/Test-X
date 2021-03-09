# Generated by Django 3.1.7 on 2021-03-08 21:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('start1', models.TimeField()),
                ('end1', models.TimeField()),
                ('start2', models.TimeField(blank=True)),
                ('end2', models.TimeField(blank=True)),
                ('maxtime', models.IntegerField()),
            ],
        ),
    ]
