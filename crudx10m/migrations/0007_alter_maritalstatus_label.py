# Generated by Django 5.1 on 2024-08-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudx10m', '0006_maritalstatus_alter_demographicdata_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maritalstatus',
            name='label',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
