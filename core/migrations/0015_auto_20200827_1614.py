# Generated by Django 2.2.8 on 2020-08-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200827_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('E', 'Equipment'), ('FW', 'Footwear'), ('A', 'Accessories'), ('C', 'Clothes'), ('SW', 'Sport wear'), ('S', 'Shirt')], max_length=2),
        ),
    ]
