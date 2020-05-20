# Generated by Django 3.0.6 on 2020-05-20 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_orderitem_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='order.OrderItem'),
            preserve_default=False,
        ),
    ]
