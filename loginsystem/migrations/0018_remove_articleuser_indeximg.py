# Generated by Django 4.2.2 on 2023-07-22 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0017_articleuser_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleuser',
            name='indeximg',
        ),
    ]