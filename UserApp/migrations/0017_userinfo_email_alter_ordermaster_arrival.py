# Generated by Django 4.1.7 on 2023-03-28 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0016_alter_ordermaster_arrival_alter_ordermaster_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='deveshmore7271@gmail.com', max_length=15),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='arrival',
            field=models.DateField(default=datetime.date(2023, 3, 31)),
        ),
    ]
