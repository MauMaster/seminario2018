# Generated by Django 2.1 on 2018-12-02 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20181123_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='receber_noticias',
        ),
    ]