# Generated by Django 3.1.7 on 2021-03-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0005_auto_20210308_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='P54cc7', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
