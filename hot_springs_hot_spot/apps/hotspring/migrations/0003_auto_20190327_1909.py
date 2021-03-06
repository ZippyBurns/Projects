# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-27 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotspring', '0002_auto_20190326_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotspring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('city', models.TextField()),
                ('country', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotsprings', to='hotspring.Comment')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='hotspring',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotsprings', to='hotspring.Message'),
        ),
        migrations.AddField(
            model_name='hotspring',
            name='users',
            field=models.ManyToManyField(related_name='hotsprings', to='hotspring.User'),
        ),
    ]
