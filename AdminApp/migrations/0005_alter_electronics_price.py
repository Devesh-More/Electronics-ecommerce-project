# Generated by Django 4.1.7 on 2023-03-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_alter_electronics_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='price',
            field=models.FloatField(default=30),
        ),
    ]
