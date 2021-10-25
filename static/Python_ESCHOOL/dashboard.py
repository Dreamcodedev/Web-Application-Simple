# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
import csv

def table_bord(root):
	frame1 =LabelFrame(root, borderwidth=3)   # Liste Elève
	frame1.grid(row=1, column=1, padx=10, pady=10)
	frame1.configure(bg="light green")


	frame2 =LabelFrame(root, borderwidth=3)   # Liste Classe
	frame2.grid(row=1, column=3, padx=10, pady=10)
	frame2.configure(bg="orange")

	frame3 =LabelFrame(root, borderwidth=3)   # Liste Professeur
	frame3.grid(row=1, column=5, padx=10, pady=10)
	frame3.configure(bg="yellow")

	frame4=LabelFrame(root, borderwidth=3)   
	frame4.grid(row=2, column=0,columnspan=8, padx=10, pady=10)
	frame4.configure(bg="light blue")

	frame5=LabelFrame(root, borderwidth=3)   
	frame4.grid(row=3, column=0,columnspan=8, padx=10, pady=10)
	frame5.configure(bg="light blue")


	Label(root, text="Etablissement").grid(row=0, column=0)
	Label(root, text="Année scolaire").grid(row=0, column=2)
	
	ListeEtablissement_b=[]
	with open ("etablissement.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeEtablissement_b.append(row)
	#ListeEtablissement=["Ecole1", "Ecole2", "Ecole3"]
	#b=a[1:]
	
	ListeEtablissement=[]
	for i in range(int(len(ListeEtablissement_b))) :
		ListeEtablissement.append(ListeEtablissement_b[i][:][0])

	AnneScolaire=["2020_2021","2021_2022","2022_2023","2023_2024"]


	e0=ttk.Combobox(root, value=ListeEtablissement)  # Etablissement
	e0.grid(row=0, column=1)

	e1=ttk.Combobox(root, value=AnneScolaire)  # Année scolaire
	e1.grid(row=0, column=3)

	#---------------
	from comptage import csvcount, chaine
	filename_Eleve="inscription.csv"
	chaine_male="Mr"
	chaine_femelle="MMe"
	chaine_g=["Mr","MMe"]
	def affichage():
		#----------Situation des élèves
		Label(frame1, text="Eleves :").grid(row=0, column=0)
		Label(frame1, text="Nombre Total :" + str(csvcount(filename_Eleve))).grid(row=1, column=0)
		#Label(frame1, text="Fille :" + str(chaine(filename_Eleve, chaine_femelle)) ).grid(row=2, column=0)
		#Label(frame1, text="Garçon :"+ str(chaine(filename_Eleve, chaine_male))).grid(row=3, column=0)
		for i in range(int(len(chaine_g))):
			L=Label(frame1, text=chaine_g[i] + ":" + str(chaine(filename_Eleve, chaine_g[i])) )
			L.grid(row=i+2, column=0)
			L.configure(bg='light green')
		def Eleves():
			from eleves import Eleves
			fenetre=Toplevel()
			Eleves(fenetre)
			fenetre.mainloop()
		Button(frame1, text ='Situation des élèves', command=Eleves).grid(row=int(len(chaine_g))+2,column=0)

		#---------- Situation des classes----------

		filename_Classe="classe.csv"
		Categorie_Classe=["CP1","CP2","CE1","CE2",
				"CM1","CM2","1ère année collège","2ème année collège","3ème année collège",
				"4ème année collège","5ème année collège","Terminale","Licence 1","Licence 2",
				"Licence 3","Master 1","Master 2","PHD","BT","BTS","Maternelle"]
		Label(frame2, text="Classe :").grid(row=0, column=0)
		Label(frame2, text="Nombre Total :" + str(csvcount(filename_Classe)-1)).grid(row=1, column=0)
		for i in range(int(len(Categorie_Classe))):
			L=Label(frame2, text=Categorie_Classe[i]+":"+str(chaine(filename_Classe, Categorie_Classe[i])))
			L.configure(bg='orange')
			L.grid(row=i+2, column=0)
			#Label(frame2, text="2ème année : 5").grid(row=3, column=0)
			#Label(frame2, text="3ème année : 5").grid(row=4, column=0)

		#Button(frame2, text ='Situation des classes').grid(row=int(len(Categorie_Classe))+2,column=0)

		#---------------
		filename_Professeur="professeurs.csv"
		ListeMatiere=[]
		with open ("matieres.csv",'r', newline='')  as files :
			spamreader=csv.reader(files,delimiter=',',quotechar='|')
			#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
			for row in spamreader :
				ListeMatiere.append(row)

		Label(frame3, text="Professeur :").grid(row=0, column=0)
		Label(frame3, text="Nombre Total :"+ str(csvcount(filename_Professeur)-1)).grid(row=1, column=0)
		for i in range(int(len(ListeMatiere))):
			L=Label(frame3, text=str(ListeMatiere[i])+":"+str(chaine(filename_Professeur, str(ListeMatiere[i][0]))))
			L.grid(row=i+2, column=0)
			L.configure(bg='yellow')
			#Label(frame3, text="Français : 2").grid(row=3, column=0)
			#Label(frame3, text="Mathématiques : 3").grid(row=4, column=0)
			#Label(frame3, text="Anglais : 2").grid(row=5, column=0)
		def Professeurs():
			from professeur import Professeurs
			fenetre=Toplevel()
			Professeurs(fenetre)
			fenetre.mainloop()
		Button(frame3, text ='Situation des professeurs',command=Professeurs).grid(row=int(len(ListeMatiere))+2,column=0)

	def c_dist():
		os.startfile(r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe")


	Button(root, text ='OK', command=affichage).grid(row=0,column=4)
	Button(root, text ='Connexion à distance', command=c_dist).grid(row=0,column=5)

