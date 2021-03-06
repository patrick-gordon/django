# Generated by Django 3.0.5 on 2020-05-01 05:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('subType', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
