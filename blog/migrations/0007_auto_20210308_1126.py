# Generated by Django 3.1.6 on 2021-03-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(choices=[('select_option', 'select option'), ('green', 'GREEN')], default='select_option', max_length=255),
        ),
    ]
