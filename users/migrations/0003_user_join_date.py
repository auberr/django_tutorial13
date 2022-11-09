# Generated by Django 4.1.2 on 2022-11-09 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='가입일'),
            preserve_default=False,
        ),
    ]
