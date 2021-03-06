# Generated by Django 3.1.7 on 2021-03-11 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_auto_20201229_0136'),
        ('software', '0002_auto_20201120_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roles', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.CharField(max_length=8)),
                ('status', models.CharField(max_length=50)),
                ('technical_description', models.TextField()),
                ('contributions', models.TextField()),
                ('collaborators', models.ManyToManyField(to='software.Collaborators')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.project')),
                ('screenshots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.album')),
            ],
        ),
    ]
