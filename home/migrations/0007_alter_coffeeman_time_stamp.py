# Generated by Django 4.2.4 on 2023-09-04 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_coffeeman_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeman',
            name='time_stamp',
            field=models.TimeField(default=datetime.datetime(2023, 9, 4, 11, 12, 32, 811316)),
        ),
    ]
