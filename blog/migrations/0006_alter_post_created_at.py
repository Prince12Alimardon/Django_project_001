# Generated by Django 4.2.7 on 2023-12-02 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_created_at_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 2, 12, 16, 29, 879878, tzinfo=datetime.timezone.utc)),
        ),
    ]