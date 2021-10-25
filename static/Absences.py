# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
import csv
from fpdf import FPDF 
import webbrowser
from datetime import datetime





def absences(root):

	frame1 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame1.grid(row=0, column=0, padx=10, pady=10)


	Label(frame1, text="Année Scolaire").grid(row=0,column=0)
	Label(frame1, text="Classe").grid(row=0,column=2)
	Label(frame1, text="N° élève").grid(row=0,column=4)

	Label(frame1, text="Nom").grid(row=1,column=0)
	Label(frame1, text="Prénom").grid(row=1,column=2)
	Label(frame1, text="NNI").grid(row=1,column=4)

	

	

	#Annee_Scolaire=["2020_2021","2021_2022","2022_2023","2023_2024","2024_2025"]
	ListeAnneeScolaire=["2020_2021","2021_2022","2022_2023","2023_2024","2024_2025"]


	e1=ttk.Combobox(frame1,values=ListeAnneeScolaire)
	e1.grid(row=0,column=1)
	

	a=[]
	#file=e1.get()+"/"+"inscription"+"/"
	#path="inscription"+".csv"
	#file="2020_2021"+"/inscription/inscription.csv"

	with open ("inscription.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			a.append(row)
	
	

	ListeEleve_Classe=[]
	for i in range(int(len(a))) :
		ListeEleve_Classe.append(a[i][:][8])

	ListeEleves_Nom=[]
	for i in range(int(len(a))) :
		ListeEleves_Nom.append(a[i][:][1])

	ListeEleves_Prenom=[]
	for i in range(int(len(a))) :
		ListeEleves_Prenom.append(a[i][:][2])

	ListeEleves_NNI=[]
	for i in range(int(len(a))) :
		ListeEleves_NNI.append(a[i][:][4])

	Liste_NEleve=[]
	for i in range(int(len(a))) :
		Liste_NEleve.append(a[i][:][9])

	Liste_AScolaire=[]
	for i in range(int(len(a))) :
		Liste_AScolaire.append(a[i][:][6])

	ListeClasse_b=[]
	with open ("classe.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeClasse_b.append(row)

	ListeClasse=[]
	for i in range(int(len(ListeClasse_b))) :
		ListeClasse.append(ListeClasse_b[i][:][1])


	e2=ttk.Combobox(frame1,values=ListeClasse)
	e3=ttk.Combobox(frame1,values=Liste_NEleve)

	e4 = Entry(frame1)  # Nom
	e5 = Entry(frame1)  # Prénom
	e6 = Entry(frame1)  # NNI

	def affichage():
		for i in range(int(len(ListeEleve_Classe))):

			if  e2.get()==ListeEleve_Classe[i] and e3.get()==Liste_NEleve[i] and e1.get()==Liste_AScolaire[i]:
				e4.delete(0,END)
				e4.insert(0,ListeEleves_Nom[i])
				e5.delete(0,END)
				e5.insert(0,ListeEleves_Prenom[i])
				e6.delete(0,END)
				e6.insert(0,ListeEleves_NNI[i])


		Label(frame1, text="Commentaire").grid(row=2,column=0)
		e7=Text(frame1)  # Commentaire
		e7.grid(row=3,column=1, columnspan=3)

		ListeMatiere=[]
		with open ("matieres.csv",'r', newline='')  as files :
			spamreader=csv.reader(files,delimiter=',',quotechar='|')
			#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
			for row in spamreader :
				ListeMatiere.append(row)

		Label(frame1, text="Cours absenté").grid(row=2,column=0)
		Label(frame1, text="Date d'absence").grid(row=2,column=2)
		Label(frame1, text="Heure d'absence").grid(row=2,column=4)




		e8=ttk.Combobox(frame1,values=ListeMatiere)  # Cours absenté
		
		e9=Entry(frame1) # Date 
		
		e10=Entry(frame1) # Heure 

		
		

		def sauver():
			file=str(e1.get())+"/"+"absence"+"/"
			e=datetime.now()
		
			date=str(e)

			try :
				os.makedirs(file)
				#os.path.join(file,"test.csv")
				#path=str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".csv"
				path=file+"absence"+".csv"
				with open (path,'a', newline='')  as files :
					w=csv.writer(files,delimiter=',',lineterminator='\n')
					w.writerow([e4.get(),e5.get(),e3.get(),e2.get(),e9.get(),e10.get(),e7.get("1.0",'end-1c'),date])
				#pdf = FPDF() 

			except :

				path=file+"absence"+".csv"
				with open (path,'a', newline='')  as files :
					w=csv.writer(files,delimiter=',',lineterminator='\n')
					w.writerow([e4.get(),e5.get(),e3.get(),e2.get(),e9.get(),e10.get(),e7.get("1.0",'end-1c'),date])

			mb.showinfo("alerte", "Les informations ont bien été enregistrées")

		Button(frame1, text ='Sauver', command=sauver).grid(row=6,column=6)

		e8.grid(row=2,column=1)
		e9.grid(row=2,column=3)
		e10.grid(row=2,column=5)


	e2.grid(row=0,column=3)
	e3.grid(row=0,column=5)
	e4.grid(row=1,column=1)
	e5.grid(row=1,column=3)
	e6.grid(row=1,column=5)


	





	Button(frame1, text ='OK', command=affichage).grid(row=0,column=6)
	
				