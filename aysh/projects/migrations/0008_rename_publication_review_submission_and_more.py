# Generated by Django 4.1.4 on 2023-02-01 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_facultyid'),
        ('projects', '0007_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='publication',
            new_name='submission',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'submission')},
        ),
    ]