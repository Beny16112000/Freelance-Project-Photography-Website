# Generated by Django 4.1.5 on 2023-01-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='detail',
            field=models.TextField(blank=True),
        ),
    ]
