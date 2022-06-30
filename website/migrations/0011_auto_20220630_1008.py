# Generated by Django 3.0.1 on 2022-06-30 05:38

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_timelineevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(null=True, upload_to=website.models.tweet_upload_path),
        ),
    ]
