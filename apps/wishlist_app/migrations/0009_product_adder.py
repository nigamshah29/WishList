# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('wishlist_app', '0008_auto_20170331_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adder',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='added_products', to='user_app.User'),
            preserve_default=False,
        ),
    ]
