# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb
from fpdf import FPDF 
import webbrowser
from time import strftime
from datetime import datetime
import os

def Situation_Comptable(root):
	frame1 =LabelFrame(root, borderwidth=1)   # Liste des élèves
	frame1.grid(row=0, column=0, padx=10, pady=10)
	frame2 =LabelFrame(root, borderwidth=1)   
	frame2.grid(row=1, column=1, padx=10, pady=10)

	Label(frame1, text="Année scolaire").grid(row=0)
	Label(frame1, text="Nom_Prenom/Foyer").grid(row=1)
	Label(frame1, text="Type").grid(row=1,column=2)
	Label(frame1, text="Mois").grid(row=2)
	Label(frame1, text="Classe").grid(row=2,column=2)
	Label(frame1, text="Somme").grid(row=3)
	Label(frame1, text="Reste à payer").grid(row=3,column=2)

	ListeAnneeScolaire=["2020_2021","2021_2022", "2022_2023","2023_2024","2024_2025"]
	ListeMois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre",
	"Novembre","Décembre"]
	Type=["Eleve","Professeur"]

	Liste_Foyer=[]
	with open ("foyer.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			Liste_Foyer.append(row)

	ListeClasse_b=[]
	with open ("classe.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeClasse_b.append(row)

	ListeClasse=[]
	for i in range(int(len(ListeClasse_b))) :
		ListeClasse.append(ListeClasse_b[i][:][1])

	e1 = ttk.Combobox(frame1,values=ListeAnneeScolaire)
	e2 = Entry(frame1)
	e22=ttk.Combobox(frame1,values=Type)
	e3 = ttk.Combobox(frame1,values=ListeMois)
	e33 = ttk.Combobox(frame1,values=ListeClasse)
	e4 = Entry(frame1)
	e5 = Entry(frame1)

	e1.grid(row=0,column=1)
	e2.grid(row=1,column=1)
	e22.grid(row=1,column=3)
	e3.grid(row=2,column=1)
	e33.grid(row=2,column=3)
	e4.grid(row=3,column=1)
	e5.grid(row=3,column=3)

	e=datetime.now()
	
	date=str(e)
	def Payer():
		file=str(e1.get())+"/"+"Comptabilite"+"/"+"Comptabilite"+"_"+str(e22.get())+"/"
		try :
			os.makedirs(file)
			#os.path.join(file,"test.csv")
			path="Comptabilite.csv"

			
			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				#w.writerow(["NNI","Mois","Payé","Reste à payer","date de saisie"])
				w.writerow([e2.get(),e3.get(),e4.get(),e5.get(),e33.get(),date])

			pdf = FPDF() 
					  
			# Add a page 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=20, h=20)
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Reçu de Paiement :",  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			pdf.cell(200, 10, txt = "Année scolaire :" +str(e1.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Nom_Prenom/Foyer :" +str(e2.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Mois :" +str(e3.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Somme :" +str(e4.get()), ln = 2, align = 'l')

			pdf.cell(200, 10, txt = "Paiement effectué le " + " "+ date, ln = 2, align = 'l')
			rec=file+str(e2.get())+"_"+str(e3.get())+".pdf"
			pdf.output(rec)
					
			
		except :

			path="Comptabilite.csv"

			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e2.get(),e3.get(),e4.get(),e5.get(),e33.get(),date])

			pdf = FPDF() 
					  
			# Add a page 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=20, h=20)
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Reçu de Paiement :",  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			pdf.cell(200, 10, txt = "Année scolaire :" +str(e1.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Nom_Prenom/Foyer :" +str(e2.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Mois :" +str(e3.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Somme :" +str(e4.get()), ln = 2, align = 'l')

			pdf.cell(200, 10, txt = "Paiement effectué le " + " "+ date, ln = 2, align = 'l')
			rec=file+str(e2.get())+"_"+str(e3.get())+".pdf"
			pdf.output(rec)
		mb.showinfo("alerte", "Les informations ont bien été enregistrées")

	def Recu():
		pdf = FPDF() 
					  
		# Add a page 
		pdf.add_page() 
		  
		# set style and size of font  
		# that you want in the pdf 
		pdf.set_font("Arial", size = 15) 
		image="logo_awlama.png"
		pdf.image(image, w=20, h=20)
		  
		# create a cell 
		

		pdf.cell(200, 10, txt = "Reçu de Paiement :",  
		         ln = 1, align = 'C') 
		pdf.cell(200, 10, txt = "--------------------------------------------------------------",  
		         ln = 1, align = 'C') 
		  
		# add another cell 
		pdf.cell(200, 8, txt = "Année scolaire :" +str(e1.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = "Nom Prenom / Foyer :" +str(e2.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = "Mois :" +str(e3.get()), ln = 2, align = 'l')
		pdf.cell(200, 8, txt = "Somme :" +str(e4.get()), ln = 2, align = 'l')

		pdf.cell(200, 7, txt = "Paiement effectué le " + " "+ date, ln = 2, align = 'l')
		rec="recu.pdf"
		pdf.output(rec)
		webbrowser.open_new(rec)


	Button(frame2, text ='Payer', command=Payer).grid(row=0,column=0)
	Button(frame2, text ='Recu', command=Recu).grid(row=0,column=1)
