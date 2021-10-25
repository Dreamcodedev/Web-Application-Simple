#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from etablissement.models import Emploi_Temps, Inscription
from etablissement.forms import InscriptionForm, ConnexionForm, EleveForm,MatiereForm, EleveForm, EmploiTempsForm
from etablissement.forms import ClassForm, EtablissementForm, ProfesseurForm, ComptabiliteForm, FoyerForm, ResultatForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import os
import sys
import csv
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import authenticate, login
from tkinter import * 
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
import csv
from fpdf import FPDF 
import webbrowser
#import sqlite3
from datetime import datetime
from django.http import FileResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
#from somewhere import handle_uploaded_file
from django.http import HttpResponseRedirect
#from .models import Author




# Create your views here.
"""
def connexion(request):
	return render(request, 'etablissement/login3.html')



def home(request):
	return render(request, 'etablissement/horizontal_navbar.html')
"""
@login_required
#@admin.register
def inscription(request):
	if request.method == 'POST':
		form = InscriptionForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			civil=form.cleaned_data["civil"]
			nom=form.cleaned_data["nom"]	
			prenom=form.cleaned_data["prenom"]
			date_naissance= form.cleaned_data["date_naissance"]
			NNI=form.cleaned_data["NNI"]
			frais_inscription=form.cleaned_data["frais_inscription"]
			Annee_s=form.cleaned_data["Annee_s"]
			etablissement = form.cleaned_data["etablissement"]
			classe =form.cleaned_data["classe"]
			adresse=form.cleaned_data["adresse"]
			N_Eleve=form.cleaned_data["N_Eleve"]
			login=form.cleaned_data["login"]
			mot_de_passe=form.cleaned_data["mot_de_passe"]
			E_mail=form.cleaned_data["E_mail"]
			Numero_Telephone=form.cleaned_data["N_Tel"]
			Tuteur_1 =form.cleaned_data["Tuteur1"]
			Tel_Tuteur_1=form.cleaned_data["Tel_Tuteur1"]
			Email_Tuteur_1=form.cleaned_data["Email_Tuteur1"]
			Tuteur_2=form.cleaned_data["Tuteur2"]
			Tel_Tureur_2=form.cleaned_data["Tel_Tuteur2"]
			Email_Tureur_2=form.cleaned_data["Email_Tuteur2"]
			Foyer=form.cleaned_data["Foyer"]


			User.objects.create_user(login, E_mail, mot_de_passe) 

			
			
			
			form.save()

	else:
		form=InscriptionForm()




	return render(request,'etablissement/inscription.html',locals())



@login_required
#@admin.register
def Matiere(request):
	if request.method == 'POST':
		form = MatiereForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			nom_matiere=form.cleaned_data["nom_matiere"]

			form.save()

	else:
		form=MatiereForm()




	return render(request,'etablissement/matiere.html',locals())

@login_required
#@admin.register
def Eleve(request):
	if request.method == 'POST':
		form = EleveForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			Annee_scolaire=form.cleaned_data["Annee_scolaire"]
			classe=form.cleaned_data["classe"]
			N_Eleve=form.cleaned_data["N_Eleve"]

			form.save()

	else:
		form=EleveForm()




	return render(request,'etablissement/eleve.html',locals())


@login_required
#@admin.register
def Professeur(request):
	if request.method == 'POST':
		form = ProfesseurForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			nom=form.cleaned_data["nom"]
			prenom=form.cleaned_data["prenom"]
			NNI=form.cleaned_data["NNI"]
			date_naissance=form.cleaned_data["date_naissance"]
			etablissement=form.cleaned_data["etablissement"]
			classe=form.cleaned_data["classe"]
			matiere=form.cleaned_data["matiere"]
			tel=form.cleaned_data["tel"]
			E_mail=form.cleaned_data["E_mail"]

			form.save()

	else:
		form=ProfesseurForm()


	return render(request,'etablissement/professeur.html',locals())

@login_required
#@admin.register
def Comptabilite(request):
	if request.method == 'POST':
		form = ComptabiliteForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			Annee_scolaire=form.cleaned_data["Annee_scolaire"]
			nom=form.cleaned_data["nom"]
			Mois=form.cleaned_data["Mois"]
			Type_ecole=form.cleaned_data["Type_ecole"]
			classe=form.cleaned_data["classe"]
			somme=form.cleaned_data["somme"]
			reste_a_payer=form.cleaned_data["reste_a_payer"]
			

			form.save()

	else:
		form=ComptabiliteForm()




	return render(request,'etablissement/comptabilite.html',locals())

@login_required
#@admin.register
def Foyer(request):
	if request.method == 'POST':
		form = FoyerForm(request.POST)
		#nom = form.cleaned_data["nom"]
		pdf = FPDF() 
		pdf.add_page()
		pdf.set_font("Arial", size = 15)
		pdf.cell(200, 10, txt = "Année scolaire :" +"test", ln = 2, align = 'l') 
		pdf.output("test.pdf")
		

		if form.is_valid():
			nom = form.cleaned_data["nom"]

			form.save()
		

	else:
		form=FoyerForm()

	return render(request,'etablissement/foyer.html',locals())


@login_required
#@admin.register
def Time_Table(request):
	

	if request.method == 'POST':
		form = EmploiTempsForm(request.POST, request.FILES)
		
		

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			
			#E_Temps=Emploi_Temps()
			annee_s=form.cleaned_data["annee_s"]
			etablissement=form.cleaned_data["etablissement"]
			classe = form.cleaned_data["classe"]
			trimestre=form.cleaned_data["trimestre"]
			time_table= request.FILES["time_table"]
			
			#handle_uploaded_file(request.FILES['file'])
			#return HttpResponseRedirect('/success/url')
	

			form.save()
			
		

	else:
		form=EmploiTempsForm()

	return render(request,'etablissement/emploitempsadmin.html',locals())

@login_required
#@admin.register
def ResultatAdmin(request):
	

	if request.method == 'POST':
		form = ResultatForm(request.POST, request.FILES)
		
		

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			annee_s=form.cleaned_data["annee_s"]
			etablissement=form.cleaned_data["etablissement"]
			classe = form.cleaned_data["classe"]
			N_Eleve = form.cleaned_data["N_Eleve"]
			trimestre=form.cleaned_data["trimestre"]
			resultat=form.cleaned_data["resultat"]
			
			

			form.save()
			
		

	else:
		form=ResultatForm()

	return render(request,'etablissement/resultatadmin.html',locals())




@login_required
#@admin.register
def Classe(request):
	if request.method == 'POST':
		form = ClassForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			etablissement=form.cleaned_data["etablissement"]
			nom_classe=form.cleaned_data["nom_classe"]
			categorie=form.cleaned_data["categorie"]

			form.save()

	else:
		form=ClassForm()




	return render(request,'etablissement/classe.html',locals())

@login_required
#@admin.register
def Etablissement(request):
	if request.method == 'POST':
		form = EtablissementForm(request.POST)

		if form.is_valid():
			#nom = form.cleaned_data["nom"]
			nom_etablissement=form.cleaned_data["nom_etablissement"]
			Adresse=form.cleaned_data["Adresse"]
			Directeur_Etablissement=form.cleaned_data["Directeur_Etablissement"]
			E_mail=form.cleaned_data["E_mail"]
			Telephone=form.cleaned_data["Telephone"]

			


			form.save()

	else:
		form=EtablissementForm()




	return render(request,'etablissement/etablissement.html',locals())


@login_required
def EmploiTemps(request):

	#files= r"C:\Users\Demba\Desktop\serveur\E_SCHOOL\static"
	#file_list = os.listdir(files)
	inscriptions=Inscription.objects.all()
	user=User.objects.all()
	return render(request,'etablissement/emploi_temps.html',locals())

@login_required
def Resultat(request):
	return render(request,'etablissement/resultat.html')

@login_required
def Whatsapp(request):
	return render(request,'etablissement/whatsapp.html')



def connexion(request):
	error = False
	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"] # Nous récupérons le nom d'utilisateur
			password = form.cleaned_data["password"] # … et le mot de passe
			user = authenticate(username=username, password=password) #Nous vérifions si les données sont correctes
			if user: # Si l'objet renvoyé n'est pas None
				login(request, user) # nous connectons l'utilisateur
			else: #sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'etablissement/connexion.html',locals())


def deconnexion(request):
	logout(request)
	return redirect(reverse('etablissement:login'))