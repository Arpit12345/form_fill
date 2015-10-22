# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fill_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fill',
            name='email',
            field=models.EmailField(max_length=254, default=0),
        ),
        migrations.AlterModelTable(
            name='fill',
            table='fill',
        ),
    ]
