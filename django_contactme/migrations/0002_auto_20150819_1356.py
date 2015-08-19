# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_contactme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmsg',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='IP address', blank=True),
        ),
    ]
