# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('i_d', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('nick', models.CharField(max_length=40)),
                ('resena', models.CharField(blank=True, max_length=80)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=240)),
                ('imagenPerfil', models.ImageField(default='perfil/default.jpg', upload_to='perfil')),
                ('imagenPortada', models.ImageField(default='portada/default.jpg', upload_to='portada')),
                ('numeroSiguiendo', models.IntegerField(default=0)),
                ('numeroSeguidores', models.IntegerField(default=0)),
                ('seguidores', models.ManyToManyField(blank=True, to='usuarios.Usuario', related_name='seguidores_rel_+')),
                ('siguiendo', models.ManyToManyField(blank=True, to='usuarios.Usuario', related_name='siguiendo_rel_+')),
                ('tweets', models.ManyToManyField(blank=True, to='tweets.Tweet')),
            ],
        ),
    ]
