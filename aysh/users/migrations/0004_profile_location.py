# Generated by Django 4.1.4 on 2023-01-29 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_journal_conference'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]