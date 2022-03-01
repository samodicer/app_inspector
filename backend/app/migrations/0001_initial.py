# Generated by Django 3.1.7 on 2022-03-01 19:38

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('files_id', models.CharField(max_length=250)),
                ('user_id', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('file', models.FileField(blank=True, null=True, upload_to=app.models.upload_path)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(null=True)),
            ],
        ),
    ]
