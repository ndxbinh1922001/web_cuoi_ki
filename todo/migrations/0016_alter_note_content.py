# Generated by Django 3.2.8 on 2021-12-04 15:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_alter_note_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
