# Generated by Django 3.2 on 2022-09-16 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220915_1231'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]