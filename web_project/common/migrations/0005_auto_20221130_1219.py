# Generated by Django 2.1.2 on 2022-11-30 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_newbfinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewBFinfo',
            new_name='NewBarrierFreeInfo',
        ),
    ]
