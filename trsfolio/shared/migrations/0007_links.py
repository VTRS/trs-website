# Generated by Django 3.1.7 on 2023-03-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0006_auto_20230227_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
    ]