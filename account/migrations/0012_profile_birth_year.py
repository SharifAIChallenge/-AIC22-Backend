# Generated by Django 3.0.1 on 2022-06-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_profile_birth_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]