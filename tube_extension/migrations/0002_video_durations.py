# Generated by Django 3.0.2 on 2020-12-27 23:19

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('tube_extension', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='durations',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[1, 2], max_length=225, size=None),
            preserve_default=False,
        ),
    ]