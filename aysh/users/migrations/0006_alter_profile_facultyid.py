# Generated by Django 4.1.4 on 2023-01-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_facultyphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='FacultyId',
            field=models.CharField(max_length=10),
        ),
    ]
