# Generated by Django 5.0.4 on 2024-05-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_post_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color_test',
        ),
        migrations.DeleteModel(
            name='Color_test2',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]