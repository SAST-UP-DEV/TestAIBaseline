# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('is_read', models.BooleanField(default=0)),
                ('text', models.CharField(blank=True, max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('pi', models.CharField(blank=True, max_length=50)),
                ('copi', models.CharField(blank=True, max_length=100)),
                ('funding', models.CharField(blank=True, max_length=50)),
                ('startyear', models.CharField(blank=True, max_length=10)),
                ('endyear', models.CharField(blank=True, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('journal', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QueryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('degree', models.IntegerField(choices=[(1, 'Ph.D.'), (2, 'M.Tech.'), (3, 'B.Tech.')], default=1)),
                ('thesis_title', models.CharField(blank=True, max_length=100)),
                ('supervisors', models.CharField(blank=True, max_length=80)),
                ('completed', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='workexp',
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(choices=[(1, 'Odd'), (2, 'Even')], default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='notif',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='publications',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='students',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='webmail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='enddate',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='startdate',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='1.jpg', upload_to=''),
        ),
    ]