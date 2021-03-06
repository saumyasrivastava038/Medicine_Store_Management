# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0007_auto_20171107_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField()),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phn_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField()),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('sal', models.CharField(max_length=20)),
                ('phn_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField()),
                ('mname', models.CharField(max_length=30)),
                ('dname', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('pname', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phn_no', models.BigIntegerField()),
                ('price', models.CharField(max_length=30)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='phn_no',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='fname',
            new_name='dname',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='lname',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
