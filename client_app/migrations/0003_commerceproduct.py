# Generated by Django 5.1.2 on 2024-10-27 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0002_commerce'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommerceProduct',
            fields=[
                ('commerce_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('commerce_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commerce_products', to='client_app.commerce')),
            ],
        ),
    ]
