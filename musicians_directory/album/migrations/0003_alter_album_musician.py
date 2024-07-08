# Generated by Django 4.2.11 on 2024-07-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
        ('album', '0002_alter_album_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='musician.musicianmodel'),
        ),
    ]
