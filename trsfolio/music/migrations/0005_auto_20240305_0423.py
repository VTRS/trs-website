# Generated by Django 3.1.7 on 2024-03-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20230228_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='ep',
            name='artwiork',
            field=models.ImageField(blank=True, null=True, upload_to='artwork'),
        ),
        migrations.AddField(
            model_name='song',
            name='flyer',
            field=models.ImageField(blank=True, null=True, upload_to='flyer'),
        ),
    ]