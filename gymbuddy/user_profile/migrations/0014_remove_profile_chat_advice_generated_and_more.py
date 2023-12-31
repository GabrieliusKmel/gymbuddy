# Generated by Django 4.2.7 on 2023-11-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_profile_chat_advice_generated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='chat_advice_generated',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_advice_regeneration',
        ),
        migrations.AddField(
            model_name='profile',
            name='chat_advice_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Chat advice time'),
        ),
    ]
