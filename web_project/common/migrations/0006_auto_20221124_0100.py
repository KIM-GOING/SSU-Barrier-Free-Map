# Generated by Django 2.1.5 on 2022-11-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20221122_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barrierfreeinfo',
            old_name='elevator_detail',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='barrierfreeinfo',
            old_name='entrance_braille',
            new_name='is_accessible_toilet',
        ),
        migrations.RenameField(
            model_name='barrierfreeinfo',
            old_name='restroom_img',
            new_name='toilet_img',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='elevator_count',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='entrance_detail',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='entrance_form',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='entrance_ramp',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='parking_detail',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='restroom_detail',
        ),
        migrations.RemoveField(
            model_name='barrierfreeinfo',
            name='restroom_floor',
        ),
        migrations.AddField(
            model_name='barrierfreeinfo',
            name='is_braille',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='barrierfreeinfo',
            name='is_elevator',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='barrierfreeinfo',
            name='is_ramp',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='barrier_free_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.BarrierFreeInfo'),
        ),
    ]