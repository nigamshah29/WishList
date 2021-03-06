# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist_app', '0004_auto_20170331_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wishitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='wishlist_app.Product'),
        ),
    ]
