# Generated by Django 4.1.7 on 2023-05-13 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0015_alter_articleuser_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleuser',
            options={'ordering': ['created']},
        ),
    ]
