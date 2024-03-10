# Generated by Django 3.2.16 on 2024-03-10 19:03

from django.db import migrations, models
import links.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='tinyurl',
            field=models.CharField(default=links.models.generate_tinyurl, max_length=10, unique=True),
        ),
    ]
