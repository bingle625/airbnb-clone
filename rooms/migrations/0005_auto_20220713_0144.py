# Generated by Django 2.2.5 on 2022-07-13 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220708_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='facility',
            new_name='facilities',
        ),
    ]