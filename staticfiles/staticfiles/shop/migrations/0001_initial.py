# Generated by Django 3.2 on 2021-05-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('release_year', models.CharField(blank=True, max_length=120)),
                ('dimensions', models.CharField(blank=True, max_length=120)),
                ('model_number', models.CharField(blank=True, max_length=120)),
                ('manufacturer', models.CharField(blank=True, max_length=120)),
                ('colour', models.CharField(blank=True, max_length=120)),
                ('connectivity', models.CharField(blank=True, max_length=120)),
                ('features', models.CharField(blank=True, max_length=120)),
                ('storage_type', models.CharField(blank=True, max_length=120)),
                ('form_factor', models.CharField(blank=True, max_length=120)),
                ('memory_type', models.CharField(blank=True, max_length=120)),
                ('processor', models.CharField(blank=True, max_length=120)),
                ('gpu', models.CharField(blank=True, max_length=120)),
                ('brand', models.CharField(blank=True, max_length=120)),
                ('graphics_interface', models.CharField(blank=True, max_length=120)),
                ('graphics_type', models.CharField(blank=True, max_length=120)),
                ('operating_system', models.CharField(blank=True, max_length=120)),
                ('tdp', models.CharField(blank=True, max_length=120)),
                ('weight', models.CharField(blank=True, max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product Detail',
                'verbose_name_plural': 'Product Details',
                'ordering': ['name'],
            },
        ),
    ]