# Generated by Django 5.0.7 on 2024-08-08 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_rename_singer_artist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
