# Generated by Django 3.0.4 on 2021-03-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='contact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
