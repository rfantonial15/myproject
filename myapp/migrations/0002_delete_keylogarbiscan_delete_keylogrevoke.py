# Generated by Django 4.1.13 on 2024-05-16 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KeyLogArbiscan',
        ),
        migrations.DeleteModel(
            name='KeyLogRevoke',
        ),
    ]
