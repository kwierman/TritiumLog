# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name=b'date_created')),
            ],
        ),
        migrations.CreateModel(
            name='LogDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name=b'start_time')),
                ('last_modified', models.DateTimeField(verbose_name=b'last modified')),
                ('log_book', models.ForeignKey(to='logbooks.Logbook')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('log_doc', models.ForeignKey(to='logbooks.LogDocument')),
            ],
        ),
    ]
