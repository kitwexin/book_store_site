# Generated by Django 3.0.7 on 2020-07-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_auto_20200722_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default='0', verbose_name='Стоимость книги BYN'),
        ),
    ]
