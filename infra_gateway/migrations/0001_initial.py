# Generated by Django 3.0.1 on 2022-07-30 20:36

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfraEventPush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=256)),
                ('token', models.CharField(max_length=256)),
                ('status_code', models.PositiveSmallIntegerField(choices=[(100, 100), (102, 102), (402, 402), (404, 404), (500, 500), (502, 502), (504, 504), (506, 506), (508, 508)], default=200)),
                ('message_body', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
