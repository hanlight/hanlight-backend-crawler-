# Generated by Django 3.0.3 on 2020-03-03 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20200303_2229'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='calendermodel',
            table='CalenderModel',
        ),
        migrations.AlterModelTable(
            name='mealmodel',
            table='MealModel',
        ),
    ]