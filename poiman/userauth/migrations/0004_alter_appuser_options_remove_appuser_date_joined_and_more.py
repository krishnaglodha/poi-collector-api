# Generated by Django 4.2.5 on 2023-09-21 09:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0003_remove_appuser_username_alter_appuser_email"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appuser",
            options={},
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="appuser",
            name="user_permissions",
        ),
    ]
