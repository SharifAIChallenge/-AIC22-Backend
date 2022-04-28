# Generated by Django 4.0.4 on 2022-04-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=100)),
                ('title_fa', models.CharField(max_length=100)),
                ('prize_en', models.CharField(max_length=100)),
                ('prize_fa', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
            ],
        ),
    ]