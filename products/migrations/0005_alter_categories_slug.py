# Generated by Django 5.0.2 on 2024-03-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]