# Generated by Django 3.2.9 on 2021-12-06 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='Created_on',
        ),
    ]