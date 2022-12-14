# Generated by Django 3.2 on 2022-12-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='code',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='QR',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
