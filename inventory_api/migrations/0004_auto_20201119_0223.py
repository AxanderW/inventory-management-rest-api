# Generated by Django 2.2 on 2020-11-19 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0003_remove_orderitem_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_item',
            new_name='productitem',
        ),
    ]