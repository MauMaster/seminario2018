# Generated by Django 2.1 on 2018-12-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensalista_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensalista',
            name='email',
        ),
    ]
