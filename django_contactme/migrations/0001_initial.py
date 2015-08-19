# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMsg',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name="Contact's name")),
                ('email', models.EmailField(max_length=254, verbose_name="Contact's email address")),
                ('message', models.TextField(max_length=3000, verbose_name='Message')),
                ('submit_date', models.DateTimeField(default=None, verbose_name='Date/Time submitted')),
                ('ip_address', models.IPAddressField(blank=True, verbose_name='IP address', null=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'contact messages',
                'db_table': 'contactme_contact_msg',
                'verbose_name': 'contact message',
                'ordering': ('submit_date',),
            },
        ),
    ]
