# Generated by Django 4.1.3 on 2022-11-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movielike'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='image'),
        ),
    ]
