# Generated by Django 3.2.3 on 2021-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_featured_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='connectivity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dimensions',
        ),
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
        migrations.RemoveField(
            model_name='product',
            name='form_factor',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gpu',
        ),
        migrations.RemoveField(
            model_name='product',
            name='graphics_interface',
        ),
        migrations.RemoveField(
            model_name='product',
            name='graphics_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='memory_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='release_year',
        ),
        migrations.RemoveField(
            model_name='product',
            name='storage_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tdp',
        ),
        migrations.AddField(
            model_name='product',
            name='audio',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='communications',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='connections',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='depth',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='finish',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='in_the_box',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='memory',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='video_support',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='operating_system',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
