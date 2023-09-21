# Generated by Django 4.2.5 on 2023-09-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0004_alter_appuser_options_remove_appuser_date_joined_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="appuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="appuser",
            name="email",
            field=models.EmailField(
                max_length=255, unique=True, verbose_name="email address"
            ),
        ),
    ]
