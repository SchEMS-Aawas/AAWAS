# Generated by Django 5.0.6 on 2024-06-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aawasUser', '0003_alter_user_password_delete_userimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
