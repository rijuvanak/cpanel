# Generated by Django 4.1.7 on 2023-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanelapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='File1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
