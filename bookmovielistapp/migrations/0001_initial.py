# Generated by Django 4.0.6 on 2022-07-21 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'BookMovieList',
                'verbose_name_plural': 'BookMovieLists',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('year_of_issue', models.DateField(blank=True, null=True)),
                ('day_complete', models.DateField(blank=True, null=True)),
                ('likes', models.BooleanField(default=False)),
                ('bookmovieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmovielistapp.bookmovielist')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmovielistapp.chapter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ListItem',
                'verbose_name_plural': 'ListItems',
            },
        ),
        migrations.AddField(
            model_name='bookmovielist',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmovielistapp.chapter'),
        ),
        migrations.AddField(
            model_name='bookmovielist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
