# Generated by Django 3.1.4 on 2021-02-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0003_eleve_matiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='nom_classe',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='nom_etablissement',
            field=models.CharField(default='', max_length=40),
        ),
    ]
