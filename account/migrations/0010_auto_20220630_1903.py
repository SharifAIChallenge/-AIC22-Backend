# Generated by Django 3.0.1 on 2022-06-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_merge_20220630_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
