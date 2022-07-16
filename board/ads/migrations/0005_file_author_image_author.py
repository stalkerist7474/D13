# Generated by Django 4.0.6 on 2022-07-16 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_file_ad_ad_images_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='ads.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='ads.user'),
        ),
    ]
