# Generated by Django 4.1.4 on 2023-01-17 14:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_rename_location_profile_address_profile_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='exam',
            name='allowed_attempts',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='exam',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]