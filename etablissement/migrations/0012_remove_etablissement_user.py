# Generated by Django 3.1.4 on 2021-03-02 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0011_auto_20210302_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etablissement',
            name='user',
        ),
    ]
