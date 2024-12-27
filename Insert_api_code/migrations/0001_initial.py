# Generated by Django 4.2.7 on 2024-12-24 13:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=110)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('images', models.JSONField()),
                ('stock', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Harvest_data_table',
            },
        ),
    ]