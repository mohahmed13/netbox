# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 14:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cipher', models.BinaryField(max_length=512)),
                ('hash', models.CharField(editable=False, max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='session_key', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
        migrations.AlterField(
            model_name='userkey',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_key', to=settings.AUTH_USER_MODEL),
        ),
    ]