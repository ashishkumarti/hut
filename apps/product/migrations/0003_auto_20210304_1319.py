# Generated by Django 3.0.4 on 2021-03-04 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210304_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='contact',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]