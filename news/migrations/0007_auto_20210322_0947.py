# Generated by Django 3.1.2 on 2021-03-22 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('name',)},
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='news.section')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
