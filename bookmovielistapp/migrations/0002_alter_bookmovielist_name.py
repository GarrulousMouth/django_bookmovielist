# Generated by Django 4.0.6 on 2022-07-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmovielistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmovielist',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
