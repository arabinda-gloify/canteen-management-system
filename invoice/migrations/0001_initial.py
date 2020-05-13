# Generated by Django 3.0.6 on 2020-05-13 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0006_canteen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_number', models.CharField(blank=True, default='', max_length=50)),
                ('date_of_issue', models.DateTimeField(auto_now=True)),
                ('unit_price', models.DecimalField(decimal_places=2, default='', max_digits=8)),
                ('discount_amount', models.DecimalField(decimal_places=2, default='', max_digits=8)),
                ('total_price', models.DecimalField(decimal_places=2, default='', max_digits=8)),
                ('canteen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Canteen')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
