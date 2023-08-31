# Generated by Django 4.2.4 on 2023-08-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffeeman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(default='0000', max_length=100)),
                ('user_name', models.CharField(default='User', max_length=100)),
                ('coffee_count', models.IntegerField(default=0, null=True)),
                ('can_drink', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Coffeeman',
                'verbose_name_plural': 'Coffeemen',
            },
        ),
    ]
