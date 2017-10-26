# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20171025_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url_path',
        ),
        migrations.AddField(
            model_name='menu',
            name='code',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='menu',
            name='level',
            field=models.CharField(blank=True, max_length=8, verbose_name='等级'),
        ),
        migrations.AddField(
            model_name='menu',
            name='path',
            field=models.CharField(blank=True, max_length=64, verbose_name='链接地址'),
        ),
    ]
