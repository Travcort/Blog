# Generated by Django 5.1.3 on 2024-11-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]