# Generated by Django 2.1.5 on 2022-11-29 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20221130_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.BarrierFreeInfo'),
        ),
    ]