# Generated by Django 4.1.4 on 2023-01-10 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0003_rename_status_wishstatus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishStatus',
            new_name='Status',
        ),
    ]
