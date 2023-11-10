# Generated by Django 4.2.7 on 2023-11-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_profile_weight_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weight_goal',
            field=models.CharField(choices=[('gain_weight', 'Gain Weight'), ('stay_lean', 'Stay Lean'), ('cut', 'Cut')], max_length=100, verbose_name='weight goal'),
        ),
    ]
