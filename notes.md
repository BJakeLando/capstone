001
# Generated by Django 4.1.4 on 2022-12-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]


002
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='posts.status'),
        ),
    ]





003


from django.db import migrations

def populate_status(apps, schemaeditor):
    statuses = {
        "published": "A post that has been published",
        "draft": "A post that has not been published"
    }
    Status = apps.get_model("posts", "Status")
    for name, desc in statuses.items():
        status_obj = Status(name=name, description = desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230104_1013'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
