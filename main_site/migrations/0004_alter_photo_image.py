# Generated by Django 4.0.1 on 2022-01-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='main_site/static/images/'),
        ),
    ]