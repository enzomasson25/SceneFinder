# Generated by Django 4.1.3 on 2022-11-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.FileField(upload_to='videos/'),
        ),
    ]