# Generated by Django 3.1.2 on 2021-03-20 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210320_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headline',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('homepage_url',)},
        ),
    ]
