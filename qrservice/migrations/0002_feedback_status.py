# Generated by Django 2.2.6 on 2019-12-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.IntegerField(choices=[(1, 'Новая'), (2, 'В работе')], default=1),
        ),
    ]
