# Generated by Django 2.1.5 on 2022-11-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='img',
            field=models.ImageField(null=True, upload_to='test/%Y/%m/%d'),
        ),
    ]