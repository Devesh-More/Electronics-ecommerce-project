# Generated by Django 4.1.7 on 2023-03-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_alter_electronics_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('expiry', models.CharField(max_length=7)),
                ('balance', models.FloatField(default=2000000)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
    ]
