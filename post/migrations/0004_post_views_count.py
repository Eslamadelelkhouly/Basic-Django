# Generated by Django 4.2.7 on 2024-09-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
