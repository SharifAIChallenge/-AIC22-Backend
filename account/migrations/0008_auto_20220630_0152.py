# Generated by Django 3.0.1 on 2022-06-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_national_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
