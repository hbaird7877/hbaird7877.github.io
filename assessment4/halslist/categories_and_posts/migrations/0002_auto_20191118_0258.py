# Generated by Django 2.2.7 on 2019-11-18 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='desription',
            new_name='post_text',
        ),
    ]
