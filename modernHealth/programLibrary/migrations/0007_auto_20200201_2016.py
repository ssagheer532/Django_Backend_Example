# Generated by Django 3.0.2 on 2020-02-02 01:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('programLibrary', '0006_auto_20200201_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='html',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ac560338-a6e3-4bc5-b7fe-a27bd6689d4f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fcc9a164-2c54-45cc-8b6a-371c7c2102ff'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cf9a8742-f893-4bd5-a273-8254e39abb99'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5b163eae-c432-406a-97c3-f31d7a074f3b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
