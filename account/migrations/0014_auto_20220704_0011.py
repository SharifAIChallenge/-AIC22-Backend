# Generated by Django 3.0.1 on 2022-07-03 19:41

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_merge_20220702_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.profile_upload_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=account.models.resume_upload_path),
        ),
    ]
