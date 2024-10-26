# Generated by Django 5.1.2 on 2024-10-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('identification', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to answer', 'I prefer not to answer')], max_length=20)),
                ('DOB', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=25)),
            ],
        ),
    ]
