# Generated by Django 3.1.7 on 2023-02-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_auto_20210316_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to='software.Collaborators'),
        ),
    ]