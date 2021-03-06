# Generated by Django 3.0.5 on 2020-05-02 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cannabis', '0002_auto_20200501_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('strain_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cannabis.Strain')),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('cannabis.strain',),
        ),
    ]
