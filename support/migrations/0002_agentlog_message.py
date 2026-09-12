from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agentlog",
            name="message",
            field=models.TextField(default=""),
        ),
    ]
