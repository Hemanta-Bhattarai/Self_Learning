# Generated by Django 2.2.13 on 2020-06-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200619_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieteaten',
            name='dietNameQuantity',
            field=models.CharField(max_length=10000),
        ),
    ]
