# Generated by Django 3.0.5 on 2020-07-18 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 21, 17, 24, 988653), verbose_name='date published'),
        ),
    ]