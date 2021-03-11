# Generated by Django 3.1.7 on 2021-03-10 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Visitors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('app_id', models.UUIDField()),
                ('name', models.CharField(max_length=50)),
                ('dr_id', models.UUIDField()),
                ('slot', models.TimeField(verbose_name='Slot(hh:mm:ss)')),
                ('date', models.DateTimeField(auto_now=True)),
                ('mode', models.CharField(choices=[('video', 'video'), ('offline', 'offline'), ('telephone', 'telephone')], max_length=30)),
                ('payment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentVerify',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pid', models.UUIDField()),
                ('app_id', models.UUIDField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('344d1725-b68b-4fc3-a950-54cb4e52e215'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=100)),
                ('postal', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('verify', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterVerify',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='CheckSlots',
        ),
    ]
