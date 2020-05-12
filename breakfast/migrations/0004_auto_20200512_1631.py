# Generated by Django 3.0.6 on 2020-05-12 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200512_1600'),
        ('breakfast', '0003_auto_20200512_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='breakfast_under_menu', to='menu.Menu'),
        ),
    ]
