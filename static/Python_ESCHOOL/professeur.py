# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb
from fpdf import FPDF 
import webbrowser


def Professeurs(root):

	frame1 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame1.grid(row=0, column=0, padx=10, pady=10)

	frame2 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame2.grid(row=0, column=1, padx=10, pady=10)

	frame3 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame3.grid(row=1, column=0, columnspan=3)

	frame4 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame4.grid(row=2, column=3)

	frame5 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame5.grid(row=0, column=2)


	Label(frame1, text="Nom").grid(row=0)
	Label(frame1, text="Prénom").grid(row=1)
	Label(frame1, text="NNI").grid(row=2)
	Label(frame1, text="Date de Naissance").grid(row=3)

	#Label(fenetre5, text="Classe").grid(row=4)

	Label(frame2, text="Etablissement").grid(row=0, column=0)
	Label(frame2, text="Classe").grid(row=1, column=0)
	Label(frame2, text="Matière").grid(row=2, column=0)
	Label(frame2, text="Tel").grid(row=3, column=0)
	Label(frame2, text="Mail").grid(row=4, column=0)

	ListeMatiere=[]
	with open ("matieres.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeMatiere.append(row)

	ListeClasse_b=[]
	with open ("classe.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeClasse_b.append(row)

	ListeClasse=[]
	for i in range(int(len(ListeClasse_b))) :
		ListeClasse.append(ListeClasse_b[i][:][1])

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

	#ListeProfesseur=["Ahmad", "Djibril", "Sidi", "Abdoullah"]
	#ListeMatiere=["Math", "Arabe", "Science", "Français"]
	#ListeClasse=["Classe1","Classe2", "Classe3"]
	#ListeEtablissement=["Ecole1","Ecole2", "Ecole3"]

	#e1 = ttk.Combobox(fenetre6,values=ListeProfesseur)
	e1=Entry(frame1)
	e2 = Entry(frame1)
	e3 = Entry(frame1)
	e4 = Entry(frame1)

	e5 = ttk.Combobox(frame2,values=ListeEtablissement)
	e6 = ttk.Combobox(frame2,values=ListeClasse)
	e7 = ttk.Combobox(frame2,values=ListeMatiere)
	e8 = Entry(frame2)
	e9 = Entry(frame2)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)

	e5.grid(row=0, column=1)
	e6.grid(row=1, column=1)
	e7.grid(row=2, column=1)
	e8.grid(row=3, column=1)
	e9.grid(row=4, column=1)



	def ecriture():
		with open ("professeurs.csv",'a', newline='')  as files :
			w=csv.writer(files,delimiter=',',lineterminator='\n')
			w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()])
		
		mb.showinfo("alerte", "Les informations ont bien été enregistrées")



	# Affichage information prfessesseur
	Label(frame3, text="NNI").grid(row=0)
	Label(frame3, text="Nom").grid(row=1)
	Label(frame3, text="Prénom").grid(row=2)
	Label(frame3, text="Date de Naissance").grid(row=3)


	Label(frame3, text="Etablissement").grid(row=0, column=4)
	Label(frame3, text="Classe").grid(row=1, column=4)
	Label(frame3, text="Matière").grid(row=2, column=4)
	Label(frame3, text="Tel").grid(row=3, column=4)
	Label(frame3, text="Mail").grid(row=4, column=4)

	e10=Entry(frame3)
	e10.configure(state=DISABLED)

	e11 = Entry(frame3)
	e11.configure(state=DISABLED)

	e12 = Entry(frame3)
	e12.configure(state=DISABLED)

	e13 = Entry(frame3)
	e13.configure(state=DISABLED)

	e14 = Entry(frame3)
	e14.configure(state=DISABLED)

	e15 = Entry(frame3)
	e15.configure(state=DISABLED)

	e16 = Entry(frame3)
	e16.configure(state=DISABLED)

	e17 = Entry(frame3)
	e17.configure(state=DISABLED)

	e18 = Entry(frame3)
	e18.configure(state=DISABLED)

	Data_Professeur=[]
	with open ("professeurs.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			Data_Professeur.append(row)

	Liste_NNI=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_NNI.append(Data_Professeur[i][:][2])

	Liste_Nom=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Nom.append(Data_Professeur[i][:][0])

	Liste_Prenom=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Prenom.append(Data_Professeur[i][:][1])

	Liste_DateNaissance=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_DateNaissance.append(Data_Professeur[i][:][3])

	Liste_Etablissement=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Etablissement.append(Data_Professeur[i][:][4])

	Liste_Classe=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Classe.append(Data_Professeur[i][:][5])

	Liste_Matiere=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Matiere.append(Data_Professeur[i][:][6])

	Liste_Tel=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Tel.append(Data_Professeur[i][:][7])

	Liste_Email=[]
	for i in range(int(len(Data_Professeur))) :
		Liste_Email.append(Data_Professeur[i][:][8])

	def affichage():
		for i in range(int(len(Liste_NNI))):

			if e10.get()==Liste_NNI[i]:
				e11.delete(0,END)
				e11.insert(0,Liste_Nom[i])
				e12.delete(0,END)
				e12.insert(0,Liste_Prenom[i])
				e13.delete(0,END)
				e13.insert(0,Liste_DateNaissance[i])
				e14.delete(0,END)
				e14.insert(0,Liste_Etablissement[i])
				e15.delete(0,END)
				e15.insert(0,Liste_Classe[i])
				e16.delete(0,END)
				e16.insert(0,Liste_Matiere[i])
				e17.delete(0,END)
				e17.insert(0,Liste_Tel[i])
				e18.delete(0,END)
				e18.insert(0,Liste_Email[i])
				def ecrire_pdf():
					# save FPDF() class into a  
					# variable pdf 
					pdf = FPDF() 
					  
					# Add a page 
					pdf.add_page() 
					  
					# set style and size of font  
					# that you want in the pdf 
					pdf.set_font("Arial", size = 15) 
					image="logo_awlama.png"
					pdf.image(image, w=20, h=20)
					  
					# create a cell 
					

					pdf.cell(200, 10, txt = "Fichier d'information du professeur :" +str(e11.get())+" "+str(e12.get()),  
					         ln = 1, align = 'C') 
					  
					# add another cell 
					pdf.cell(200, 10, txt = "NNI :" +str(e10.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Nom :" +str(e11.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Prenom :" +str(e12.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Date de Naissance :" +str(e13.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Etablissement :" +str(e14.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Classe :" +str(e15.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Matière :" +str(e16.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Téléphone :" +str(e17.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Email :" +str(e18.get()), ln = 2, align = 'l') 
					  
					  
					# save the pdf with name .pdf 
					pdf.output("GFG.pdf")
					
					webbrowser.open_new("GFG.pdf")  
				Button(frame4, text ='Imprimer', command=ecrire_pdf).grid(row=0,column=1)  

	def edition():
		#objet_entry.configure(state=etat)
		e10.configure(state=NORMAL)
		e11.configure(state=NORMAL)
		e12.configure(state=NORMAL)
		e13.configure(state=NORMAL)
		e14.configure(state=NORMAL)
		e15.configure(state=NORMAL)
		e16.configure(state=NORMAL)
		e17.configure(state=NORMAL)
		e18.configure(state=NORMAL)
		#e10.configure(state=NORMAL)
		#e11.configure(state=NORMAL)
			

	e10.grid(row=0, column=1)
	e11.grid(row=1, column=1)
	e12.grid(row=2, column=1)
	e13.grid(row=3, column=1)

	e14.grid(row=0, column=5)
	e15.grid(row=1, column=5)
	e16.grid(row=2, column=5)
	e17.grid(row=3, column=5)
	e18.grid(row=4, column=5)

	
	
	Button(frame4, text ='Editer', command=edition).grid(row=0,column=0)
	
	Button(frame3, text ='OK', command=affichage).grid(row=0,column=2)
	Button(frame5, text ='Sauver', command=ecriture).grid(row=0,column=0)


