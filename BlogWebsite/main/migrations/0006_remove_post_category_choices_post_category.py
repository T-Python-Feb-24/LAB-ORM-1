# Generated by Django 4.2.11 on 2024-03-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_post_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="category_choices",),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("General", "General"),
                    ("Tech", "Tech"),
                    ("Science", "Science"),
                    ("Fashion", "Fashion"),
                ],
                default="General",
                max_length=64,
            ),
            preserve_default=False,
        ),
    ]
