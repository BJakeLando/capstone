# Generated by Django 4.1.4 on 2023-01-12 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0004_rename_wishstatus_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='reporter',
            new_name='author',
        ),
    ]
