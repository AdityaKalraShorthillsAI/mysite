# Generated by Django 5.1 on 2024-08-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudx10m', '0004_alter_education_label_alter_nativecountry_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nativecountry',
            name='label',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='sex',
            name='label',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
