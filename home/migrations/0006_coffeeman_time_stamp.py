# Generated by Django 4.2.4 on 2023-09-04 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_coffeeman'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeman',
            name='time_stamp',
            field=models.TimeField(default=datetime.datetime(2023, 9, 4, 11, 10, 50, 401918)),
        ),
    ]
