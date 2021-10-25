# Generated by Django 3.1.4 on 2021-03-01 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0006_auto_20210225_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=20)),
                ('prenom', models.CharField(default='', max_length=20)),
                ('NNI', models.CharField(default='', max_length=20)),
                ('date_naissance', models.DateField(verbose_name='date of birth')),
                ('N_Tel', models.CharField(default='', max_length=20)),
                ('Email_Tuteur1', models.EmailField(default='', max_length=254)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.classe')),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.etablissement')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Comptabilite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_s', models.CharField(choices=[('annee scolaire', '2020_2021'), ('annee scolaire', '2021_2022'), ('annee scolaire', '2022_2023'), ('annee scolaire', '2023_2024'), ('annee scolaire', '2024_2025')], max_length=20)),
                ('nom', models.CharField(default='', max_length=20)),
                ('Mois', models.CharField(default='', max_length=20)),
                ('Type', models.CharField(choices=[('Eleve', 'Elève'), ('Professeur', 'Professeur')], max_length=20)),
                ('somme', models.CharField(default='', max_length=20)),
                ('reste_a_payer', models.CharField(default='', max_length=20)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.classe')),
            ],
        ),
    ]
