# Generated by Django 2.1.7 on 2019-03-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='currentMap',
            field=models.CharField(default=[-1], max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map',
            name='mineMap',
            field=models.CharField(max_length=1000),
        ),
    ]
