# Generated by Django 5.0.7 on 2024-07-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
