# Generated by Django 4.2.7 on 2024-12-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insert_api_code', '0005_alter_harvest_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='Name',
            field=models.CharField(max_length=1000),
        ),
    ]