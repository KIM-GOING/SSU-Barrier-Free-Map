# Generated by Django 2.1.5 on 2022-11-29 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20221130_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='location',
        ),
        migrations.AddField(
            model_name='reply',
            name='barrier_free_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.BarrierFreeInfo'),
        ),
    ]
