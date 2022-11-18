# Generated by Django 4.1.2 on 2022-11-18 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('length', models.DurationField()),
                ('path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('length', models.DurationField()),
                ('image', models.CharField(max_length=500)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.video')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sequence')),
            ],
        ),
    ]