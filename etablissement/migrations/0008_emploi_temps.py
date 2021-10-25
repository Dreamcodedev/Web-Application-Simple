# Generated by Django 3.1.4 on 2021-03-02 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0007_comptabilite_foyer_professeur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emploi_Temps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_s', models.CharField(choices=[('annee scolaire', '2020_2021'), ('annee scolaire', '2021_2022'), ('annee scolaire', '2022_2023'), ('annee scolaire', '2023_2024'), ('annee scolaire', '2024_2025')], max_length=20)),
                ('etablissement', models.CharField(default='', max_length=40)),
                ('trimestre', models.CharField(choices=[('Trimestre 1', 'Trimestre 1'), ('Trimestre 2', 'Trimestre 2'), ('Trimestre 3', 'Trimestre 3')], max_length=20)),
                ('time_table', models.FileField(upload_to='emplois_temps/')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.classe')),
            ],
        ),
    ]