# Generated by Django 3.1.6 on 2021-03-01 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='post_image',
        ),
    ]