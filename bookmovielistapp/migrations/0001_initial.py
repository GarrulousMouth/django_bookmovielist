# Generated by Django 4.0.4 on 2022-07-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookMovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('year_of_issue', models.DateField()),
                ('day_complete', models.DateField()),
                ('likes', models.BooleanField(default=False)),
            ],
        ),
    ]
