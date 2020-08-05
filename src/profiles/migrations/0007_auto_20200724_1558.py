# Generated by Django 3.0.7 on 2020-07-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_profile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='ул.Советская 7-22', max_length=20, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Минск', max_length=20, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Беларусь', max_length=20, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.CharField(default='220123', max_length=20, verbose_name='Индекс'),
        ),
    ]
