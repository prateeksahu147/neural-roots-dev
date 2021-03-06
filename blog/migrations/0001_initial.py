# Generated by Django 3.2 on 2021-05-03 08:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogPostName', models.CharField(max_length=50)),
                ('blogPostDate', models.DateTimeField()),
                ('blogPost', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('blogCategory', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
