# Generated by Django 3.2.8 on 2021-10-25 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CerDocument',
            new_name='CarDocument',
        ),
    ]