# Generated by Django 2.2 on 2021-03-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210331_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_model',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
