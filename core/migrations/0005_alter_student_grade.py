# Generated by Django 4.1.4 on 2023-01-17 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_profile_role_student_grade_student_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('1CP', '1CP'), ('2CP', '2CP'), ('3IIR', '3IIR'), ('4IIR', '4IIR')], max_length=50, null=True),
        ),
    ]
