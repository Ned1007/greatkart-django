# Generated by Django 3.2.3 on 2021-06-04 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
