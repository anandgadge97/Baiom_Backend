# Generated by Django 4.2 on 2024-01-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='itie',
            field=models.BooleanField(default=False),
        ),
    ]