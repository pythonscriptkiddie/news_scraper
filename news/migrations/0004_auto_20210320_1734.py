# Generated by Django 3.1.2 on 2021-03-20 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210320_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headline',
            old_name='url',
            new_name='article_url',
        ),
    ]
