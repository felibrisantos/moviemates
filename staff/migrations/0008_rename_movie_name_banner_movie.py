# Generated by Django 4.1.3 on 2022-12-05 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_alter_banner_movie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='movie_name',
            new_name='movie',
        ),
    ]