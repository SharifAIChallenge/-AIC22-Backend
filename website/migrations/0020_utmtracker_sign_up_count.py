# Generated by Django 3.0.1 on 2022-07-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_merge_20220704_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='utmtracker',
            name='sign_up_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]