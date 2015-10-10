# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nick',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
    ]
