# Generated by Django 3.1.2 on 2020-11-20 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_auto_20201120_1930'),
        ('photography', '0003_auto_20201120_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shared.album'),
        ),
    ]
