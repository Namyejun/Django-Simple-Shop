# Generated by Django 2.1.7 on 2023-02-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='상품명')),
                ('product_price', models.IntegerField(verbose_name='상품가격')),
                ('product_desc', models.TextField(verbose_name='상품설명')),
                ('product_stock', models.IntegerField(verbose_name='상품재고')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': 'tb_product',
            },
        ),
    ]
