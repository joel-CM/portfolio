# Generated by Django 4.2.4 on 2023-09-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myself', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myself',
            name='github',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='myself',
            name='linkedin',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
