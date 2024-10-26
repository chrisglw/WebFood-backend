# Generated by Django 5.1.2 on 2024-10-27 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0002_city_address'),
        ('production_app', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(max_length=50, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer_app.address')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='production_app.category')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='production_app.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='production_app.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='production_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='MenuProduct',
            fields=[
                ('menu_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_products', to='production_app.menu')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_products', to='production_app.product')),
            ],
        ),
    ]
