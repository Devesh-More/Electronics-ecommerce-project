# Generated by Django 4.1.7 on 2023-03-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0022_alter_userinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default='Vivekanand Nagar Bhadgaon Road, Pachora', max_length=300),
        ),
    ]
