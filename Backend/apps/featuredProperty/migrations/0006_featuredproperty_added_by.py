# Generated by Django 5.0.6 on 2024-06-16 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aawasUser', '0004_alter_user_email'),
        ('featuredProperty', '0005_alter_propertyimage_featured_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredproperty',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aawasUser.user'),
        ),
    ]