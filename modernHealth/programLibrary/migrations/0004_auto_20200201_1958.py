# Generated by Django 3.0.2 on 2020-02-02 00:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('programLibrary', '0003_auto_20200201_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='html',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e513987-92c9-4751-b9bc-3808fcd5ccf3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4eb11a1b-26c1-4323-aef7-49791f010b1b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1779c78f-7634-4a2a-b6cb-10d0af320795'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7e2f0d60-f6d1-41be-9dfb-6ae4ff39abeb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
