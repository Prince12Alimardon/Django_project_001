# Generated by Django 4.2.7 on 2023-12-04 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 16, 42, 23, 350056, tzinfo=datetime.timezone.utc)),
        ),
    ]