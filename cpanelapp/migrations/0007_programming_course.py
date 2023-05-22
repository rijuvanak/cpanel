# Generated by Django 4.1.7 on 2023-04-06 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpanelapp', '0006_rename_name_subcategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('programming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpanelapp.programming')),
            ],
        ),
    ]