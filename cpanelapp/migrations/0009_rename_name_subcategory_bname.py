# Generated by Django 3.2.16 on 2023-04-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanelapp', '0008_rename_bname_subcategory_name_delete_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='bname',
        ),
    ]