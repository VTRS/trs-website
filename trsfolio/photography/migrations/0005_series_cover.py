# Generated by Django 3.1.7 on 2024-03-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0004_auto_20201120_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='series/'),
        ),
    ]