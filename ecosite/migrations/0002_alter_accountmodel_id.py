# Generated by Django 4.2.1 on 2023-05-29 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecosite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb7aee24-0b39-40d0-9733-278e5c3f5211'), editable=False, primary_key=True, serialize=False),
        ),
    ]
