# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name=b'start_time')),
                ('last_modified', models.DateTimeField(verbose_name=b'last modified')),
            ],
        ),
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name=b'start date')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='log_book',
            field=models.ForeignKey(to='logbook.Logbook'),
        ),
    ]
