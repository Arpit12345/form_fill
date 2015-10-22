# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=200)),
                ('Add', models.CharField(max_length=200)),
                ('ipadd', models.IntegerField(default=0)),
                ('phoneno', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('t1', models.CharField(max_length=200)),
            ],
        ),
    ]
