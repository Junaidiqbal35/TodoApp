# Generated by Django 4.1.5 on 2023-01-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todolist_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
