# Generated by Django 3.0.6 on 2020-05-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('TS', 'Today Special'), ('B', 'Breakfast'), ('L', 'Lunch'), ('S', 'Snacks'), ('D', 'Dinner')], default='', max_length=2),
        ),
    ]
