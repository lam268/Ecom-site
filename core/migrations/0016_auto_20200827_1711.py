# Generated by Django 2.2.8 on 2020-08-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200827_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('E', 'Equipment'), ('FW', 'Footwear'), ('A', 'Accessories'), ('C', 'Clothes')], max_length=2),
        ),
    ]
