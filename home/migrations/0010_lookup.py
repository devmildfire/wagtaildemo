# Generated by Django 4.2.4 on 2023-09-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_coffeeman_can_drink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='0000', max_length=100)),
                ('readable_name', models.CharField(default='User', max_length=100)),
            ],
            options={
                'verbose_name': 'LookUp',
                'verbose_name_plural': 'LookUps',
            },
        ),
    ]
