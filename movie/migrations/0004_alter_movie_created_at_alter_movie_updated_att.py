# Generated by Django 4.1.7 on 2023-03-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_rename_update_att_movie_updated_att'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_att',
            field=models.DateTimeField(auto_now=True),
        ),
    ]