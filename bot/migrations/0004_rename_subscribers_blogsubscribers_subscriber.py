# Generated by Django 3.2.4 on 2021-06-06 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_blogsubscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogsubscribers',
            old_name='subscribers',
            new_name='subscriber',
        ),
    ]