# Generated by Django 2.1.7 on 2019-05-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_auto_20190525_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='შეკვეთის თარიღი')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='განახლებულია')),
                ('paid', models.BooleanField(default=False, verbose_name='გადახდილია')),
            ],
            options={
                'verbose_name': 'შეკვეთა',
                'verbose_name_plural': 'შეკვეთები',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ფასი')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='რაოდენობა')),
                ('order', models.ForeignKey(on_delete='CASCADE', related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete='CASCADE', related_name='order_items', to='shop.Product')),
            ],
        ),
    ]