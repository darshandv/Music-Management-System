# Generated by Django 2.2 on 2019-04-08 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20181027_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'permissions': (('can_add_artists', 'Can add artists'),)},
        ),
    ]
