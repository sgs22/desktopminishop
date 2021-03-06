# Generated by Django 3.2.3 on 2021-05-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About Panel'},
        ),
        migrations.AlterModelOptions(
            name='productdetail',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='about',
            name='feature_1_content',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='about',
            name='feature_1_title',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='about',
            name='feature_2_content',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='about',
            name='feature_2_title',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='about',
            name='feature_3_content',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='about',
            name='feature_3_title',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
