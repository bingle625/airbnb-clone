# Generated by Django 2.2.5 on 2022-07-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220705_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='langauage',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], max_length=13, null=True),
        ),
    ]
