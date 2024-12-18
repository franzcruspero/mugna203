# Generated by Django 5.1.1 on 2024-12-05 08:28

import users.storages
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_birthday"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=users.storages.UniqueFileStorage(),
                upload_to="",
            ),
        ),
    ]
