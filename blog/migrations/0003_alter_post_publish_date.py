# Generated by Django 4.2.6 on 2023-10-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_publish_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="publish_date",
            field=models.TextField(),
        ),
    ]
