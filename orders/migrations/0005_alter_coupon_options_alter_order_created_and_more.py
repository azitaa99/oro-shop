# Generated by Django 5.0.2 on 2024-03-03 14:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_senderinfo_order'),
        ('products', '0002_alter_comment_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': ' کد تخفیف', 'verbose_name_plural': 'کدهای تخفیف '},
        ),
        migrations.AlterField(
            model_name='order',
            name='Created',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریج ثبت سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='وضعیت پرداخت'),
        ),
        migrations.AlterField(
            model_name='order',
            name='random_code',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='کد سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='senderinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='سفارش '),
        ),
    ]
