# Generated by Django 4.2.7 on 2024-12-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Harvest_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='login',
            table='login_details',
        ),
    ]
