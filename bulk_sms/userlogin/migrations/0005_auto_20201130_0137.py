# Generated by Django 3.1.2 on 2020-11-29 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userlogin', '0004_auto_20201130_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credits',
            name='id',
        ),
        migrations.AlterField(
            model_name='credits',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
