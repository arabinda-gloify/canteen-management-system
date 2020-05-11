# Generated by Django 3.0.6 on 2020-05-11 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0002_auto_20200510_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, default="Today's Menu", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
