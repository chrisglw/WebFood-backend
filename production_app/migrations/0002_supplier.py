# Generated by Django 5.1.2 on 2024-10-27 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0002_city_address'),
        ('production_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_phone', models.CharField(max_length=15)),
                ('supplier_email', models.EmailField(max_length=100)),
                ('supplier_address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='customer_app.city')),
            ],
        ),
    ]
