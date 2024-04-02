# Generated by Django 5.0.2 on 2024-03-02 20:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('Created', models.DateTimeField(auto_now=True)),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('random_code', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'جزییات سبد خرید',
                'verbose_name_plural': 'اطلاعات سبد خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='Senderinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='نام ونام خانوادگی')),
                ('phone', models.CharField(max_length=15, verbose_name='تلفن')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=1000, verbose_name='آدرس')),
                ('city', models.CharField(max_length=500, verbose_name='شهر')),
                ('postal_code', models.CharField(max_length=25, verbose_name='کد پستی')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresess', to='orders.order')),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست ها',
            },
        ),
    ]
