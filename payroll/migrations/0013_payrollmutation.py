# Generated by Django 3.2.21 on 2024-02-07 09:07

import core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_mutationlog_autogenerated_code'),
        ('payroll', '0012_auto_20240202_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payroll', to='core.mutationlog')),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='payroll.payroll')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
    ]
