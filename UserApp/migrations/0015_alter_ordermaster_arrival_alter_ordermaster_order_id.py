# Generated by Django 4.1.7 on 2023-03-26 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0014_alter_ordermaster_order_id_alter_ordermaster_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='arrival',
            field=models.DateField(default=datetime.date(2023, 3, 29)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='order_id',
            field=models.CharField(default=330665, max_length=5),
        ),
    ]
