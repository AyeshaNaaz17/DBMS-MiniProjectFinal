# Generated by Django 4.1.4 on 2023-02-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_rename_publication_review_submission_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submissions',
            options={'ordering': ['-vote_total', 'title']},
        ),
    ]