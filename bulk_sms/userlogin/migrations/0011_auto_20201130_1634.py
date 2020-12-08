# Generated by Django 3.1.2 on 2020-11-30 11:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userlogin', '0010_auto_20201130_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_reports',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 11, 4, 5, 701631, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message_reports',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
