# Generated by Django 3.2.4 on 2021-06-07 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210606_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='ban',
            field=models.BooleanField(default=False, verbose_name='Banned'),
        ),
    ]