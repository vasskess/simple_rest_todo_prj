# Generated by Django 4.2.3 on 2023-07-18 20:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo_rest", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tasktodo",
            options={"verbose_name_plural": "Task`s"},
        ),
    ]
