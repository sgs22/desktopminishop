# Generated by Django 3.2.3 on 2021-05-14 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210514_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='feature_1_content',
        ),
        migrations.RemoveField(
            model_name='about',
            name='feature_1_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='feature_2_content',
        ),
        migrations.RemoveField(
            model_name='about',
            name='feature_2_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='feature_3_content',
        ),
        migrations.RemoveField(
            model_name='about',
            name='feature_3_title',
        ),
    ]
