# Generated by Django 5.2 on 2025-04-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductosApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='productoImagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
