# Generated by Django 4.0.6 on 2022-07-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birhtday',
            field=models.DateField(null=True),
        ),
    ]