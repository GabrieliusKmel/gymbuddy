# Generated by Django 4.2.7 on 2023-11-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_alter_profile_chat_advice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='chat_advice',
            field=models.TextField(blank=True, null=True, verbose_name='ChatGPT advice'),
        ),
    ]
