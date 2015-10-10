# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('i_dT', models.AutoField(serialize=False, primary_key=True)),
                ('contenido', models.TextField(max_length=140)),
                ('nombreUser', models.CharField(max_length=80)),
                ('apellidoUser', models.CharField(max_length=80)),
                ('nickUser', models.CharField(max_length=40)),
                ('imgUser', models.ImageField(upload_to='tweets/perfil')),
                ('favoritos', models.IntegerField(default=0)),
                ('retweets', models.IntegerField(default=0)),
            ],
        ),
    ]
