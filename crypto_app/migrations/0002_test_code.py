# Generated by Django 4.1.5 on 2023-01-31 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]