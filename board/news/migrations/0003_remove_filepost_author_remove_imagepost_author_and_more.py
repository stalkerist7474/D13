# Generated by Django 4.0.6 on 2022-07-23 11:40

import django.core.validators
from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_imagepost_filepost_post_post_files_post_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filepost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='imagepost',
            name='author',
        ),
        migrations.AlterField(
            model_name='filepost',
            name='file',
            field=models.FileField(null=True, upload_to=news.models.post_author_directory_path, validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_files',
        ),
        migrations.AddField(
            model_name='post',
            name='post_files',
            field=models.ManyToManyField(blank=True, to='news.filepost'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_images',
        ),
        migrations.AddField(
            model_name='post',
            name='post_images',
            field=models.ManyToManyField(blank=True, to='news.imagepost'),
        ),
    ]
