# Generated by Django 3.1.2 on 2020-11-30 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0012_auto_20201201_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_reports',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 18, 54, 30, 547166, tzinfo=utc)),
        ),
    ]
