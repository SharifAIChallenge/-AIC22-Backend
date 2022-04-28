# Generated by Django 3.0.1 on 2022-04-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_merge_20220428_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='post_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pastaic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]