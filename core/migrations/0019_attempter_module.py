# Generated by Django 4.1.4 on 2023-01-20 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_matiere_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempter',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.matiere'),
        ),
    ]
