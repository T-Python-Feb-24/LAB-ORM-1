# Generated by Django 5.0.3 on 2024-03-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='images/default.jpeg', upload_to='images/'),
        ),
    ]
