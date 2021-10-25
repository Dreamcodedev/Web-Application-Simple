#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (('Mr',  'Mister'),
                  ('Mrs', 'Madam'),
                  ('Miss', 'Miss'))

Categorie_Classe=(('2nd',  'Second'),
                  ('3eme', 'Troisieme'),
                  ('Tle', 'Terminale'))

Trimestre=(('Trimestre 1',  'Trimestre 1'),
                  ('Trimestre 2', 'Trimestre 2'),
                  ('Trimestre 3', 'Trimestre 3'))

Type_ecole=(('Eleve',  'Elève'),
                  ('Professeur', 'Professeur')
             )


ANNEE_SCOLAIRE=(('annee scolaire','2020_2021'),
                  ('annee scolaire','2021_2022'),
                  ('annee scolaire','2022_2023'),
                  ('annee scolaire','2023_2024'),
                  ('annee scolaire','2024_2025'))




class Etablissement(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	nom_etablissement=models.CharField(max_length=40,default="")
	Adresse=models.CharField(max_length=40,default="")
	Directeur_Etablissement=models.CharField(max_length=40,default="")
	E_mail=models.CharField(max_length=40,default="")
	Telephone=models.CharField(max_length=40,default="")


	def __str__(self):
		return self.nom_etablissement

class Classe(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	etablissement = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
	nom_classe=models.CharField(max_length=40,default="")
	categorie=models.CharField(max_length=6, choices=Categorie_Classe)


	def __str__(self):
		return self.nom_classe


class Matiere(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	nom_matiere=models.CharField(max_length=40)


	def __str__(self):
		return self.nom_matiere

class Eleve(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	Annee_scolaire=models.CharField(max_length=40,choices=ANNEE_SCOLAIRE)
	classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	N_Eleve=models.CharField(max_length=20,default="")


	def __str__(self):
		return self.N_Eleve


class Professeur(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	nom=models.CharField(max_length=20,default="")
	prenom=models.CharField(max_length=20,default="")
	NNI=models.CharField(max_length=20,default="")
	date_naissance= models.DateField(('date of birth'))
	etablissement = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
	#classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	classe = models.ManyToManyField(Classe)
	#matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)
	matiere = models.ManyToManyField(Matiere)
	N_Tel=models.CharField(max_length=20,default="")
	Email_Tuteur1=models.EmailField(default="")


	def __str__(self):
		return self.nom

class Comptabilite(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	annee_s=models.CharField(max_length=20, choices=ANNEE_SCOLAIRE)
	nom=models.CharField(max_length=20,default="")
	Mois=models.CharField(max_length=20,default="")
	Type=models.CharField(max_length=20, choices=Type_ecole)
	classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	somme=models.CharField(max_length=20,default="")
	reste_a_payer=models.CharField(max_length=20,default="")
	


	def __str__(self):
		return self.nom

class Foyer(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	nom=models.CharField(max_length=20,default="")
	

	def __str__(self):
		return self.nom

class Inscription(models.Model):
	#user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	civil=models.CharField(max_length=6, choices=GENDER_CHOICES)
	nom=models.CharField(max_length=20,default="")
	prenom=models.CharField(max_length=20,default="")
	date_naissance= models.DateField(('date of birth'))
	NNI=models.CharField(max_length=20,default="") 
	frais_inscription=models.CharField(max_length=20,default="") 
	Annee_s=models.CharField(max_length=20,default="")
	etablissement = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
	classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	N_Eleve=models.CharField(max_length=20,default="")
	adresse=models.CharField(max_length=20,default="")

	login=models.CharField(max_length=20,default="")
	mot_de_passe=models.CharField(max_length=20,default="")
	E_mail=models.EmailField(default="")
	N_Tel=models.CharField(max_length=20,default="")

	Tuteur1 =models.CharField(max_length=20,default="")
	Tel_Tuteur1 =models.CharField(max_length=20,default="")
	Email_Tuteur1=models.EmailField(default="")

	Tuteur2 =models.CharField(max_length=20,default="")
	Tel_Tuteur2 =models.CharField(max_length=20,default="")
	Email_Tuteur2=models.EmailField(default="")

	Foyer=models.ForeignKey(Foyer,on_delete=models.CASCADE)


	#User.objects.create_user(str(login),str(E_mail),str(mot_de_passe))
	
	


	def __str__(self):
		return self.nom


class Emploi_Temps(models.Model):
	user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	annee_s=models.CharField(max_length=20, choices=ANNEE_SCOLAIRE)
	etablissement = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
	classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	trimestre=models.CharField(max_length=20, choices=Trimestre)
	time_table=models.FileField(upload_to="time_table/")


	def __str__(self):
		return self.time_table
    	
class Resultat(models.Model):
	user = models.OneToOneField(User,default="",null=True,on_delete=models.CASCADE)
	annee_s=models.CharField(max_length=20, choices=ANNEE_SCOLAIRE)
	etablissement = models.ForeignKey(Etablissement,on_delete=models.CASCADE)
	classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
	N_Eleve=models.CharField(max_length=20,default="")
	trimestre=models.CharField(max_length=20, choices=Trimestre)
	resultat=models.FileField(upload_to="resultat/")


	def __str__(self):
		return self.classe


