# Generated by Django 4.2.9 on 2024-02-02 19:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_new_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]