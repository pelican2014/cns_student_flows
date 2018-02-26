# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFlow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=128)),
                ('flow_type', models.CharField(max_length=16)),
                ('category', models.CharField(max_length=16)),
                ('batch', models.CharField(max_length=8)),
                ('year', models.CharField(max_length=2)),
                ('major_from', models.CharField(max_length=128)),
                ('code_from', models.CharField(max_length=16)),
                ('status', models.CharField(max_length=128)),
                ('college_to', models.CharField(max_length=128)),
                ('major_to', models.CharField(max_length=128)),
                ('code_to', models.CharField(max_length=16)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
