# Generated by Django 4.2.2 on 2023-06-08 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_posts_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
    ]
