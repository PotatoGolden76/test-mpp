# Generated by Django 4.1.7 on 2023-03-12 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('age', models.IntegerField(blank=True)),
                ('birthDate', models.DateTimeField()),
                ('deathDate', models.DateTimeField(blank=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'directors',
                'ordering': ['-age'],
            },
        ),
    ]