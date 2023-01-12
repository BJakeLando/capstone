
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
        ('posts', '0003_alter_post_status'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
