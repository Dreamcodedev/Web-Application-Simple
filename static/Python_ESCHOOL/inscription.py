# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
import csv
from fpdf import FPDF 
import webbrowser
# =================Menu inscription==============
def Inscription(root):
	
	
	#root= Tk()
	#fenetre1.title("Inscription")
	#root.title("Inscription")
	
	frame1 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame1.grid(row=0, column=0, padx=10, pady=10)

	frame2 =LabelFrame(root, borderwidth=3)   
	frame2.grid(row=1, column=0, padx=10, pady=10)

	frame3 =LabelFrame(root, borderwidth=3)   
	frame3.grid(row=2, column=0, padx=10, pady=10)

	frame4 =LabelFrame(root, borderwidth=3)   
	frame4.grid(row=0, column=1, padx=10, pady=10)
	
	frame5 =LabelFrame(root, borderwidth=3)   
	frame5.grid(row=1, column=1, padx=10, pady=10)

	frame55 =LabelFrame(root, borderwidth=3)   
	frame55.grid(row=2, column=1, padx=10, pady=10)
	
	frame6 =LabelFrame(root, borderwidth=3)   
	frame6.grid(row=6, column=6, padx=10, pady=10)
	
	
	
	
	#Canvas(fenetre1, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
	#Canvas(fenetre1).pack()

	# frame 1
	Label(frame1, text="Civilité").grid(row=0)
	Label(frame1, text="Nom").grid(row=1)
	Label(frame1, text="Prénom").grid(row=2)
	Label(frame1, text="Date de Naissance").grid(row=3)
	Label(frame1, text="NNI").grid(row=4)
	Label(frame1, text="Frai d'inscription").grid(row=5)
	Label(frame1, text="année scolaire").grid(row=6)
        # frame2--------------
	Label(frame2, text="Etablissement").grid(row=0)
	Label(frame2, text="Classe").grid(row=1)
	Label(frame2, text="N° Elève").grid(row=2)
	Label(frame2, text="Adresse").grid(row=3)
	
	# frame3

	Label(frame3, text="Login").grid(row=0)
	Label(frame3, text="Mot de passe").grid(row=1)
	Label(frame3, text="Confirmer le mot de passe").grid(row=2)
	Label(frame3, text="Adresse mail").grid(row=3)
	Label(frame3, text="Numéro de tél").grid(row=4)

	# frame4
	Label(frame4, text="Tuteur 1").grid(row=0, column=0)
	Label(frame4, text="Tel Tuteur 1").grid(row=1, column=0)
	Label(frame4, text="adresse mail").grid(row=2, column=0)

	# frame 5
	
	Label(frame5, text="Tuteur 2").grid(row=0, column=0)
	Label(frame5, text="Tel Tuteur 2").grid(row=1, column=0)
	Label(frame5, text="adresse mail").grid(row=2, column=0)

	Label(frame55, text="Foyer").grid(row=0, column=0)
	
	#----------------------------------------
	
	ListeGenre=["Mr", "MMe"]
	ListeAnneeScolaire=["2020_2021","2021_2022","2022_2023","2023_2024","2024_2025"]

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

	ListeClasse_b=[]
	with open ("classe.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeClasse_b.append(row)

	ListeClasse=[]
	for i in range(int(len(ListeClasse_b))) :
		ListeClasse.append(ListeClasse_b[i][:][1])


	#e1 = Entry(fenetre1)
	e1=ttk.Combobox(frame1,values=ListeGenre)
	e2 = Entry(frame1)
	e3 = Entry(frame1)
	e4 = Entry(frame1)
	e44 = Entry(frame1)
	e444 = Entry(frame1)
	e4444=ttk.Combobox(frame1,values=ListeAnneeScolaire)
	# frame2
	e5 = ttk.Combobox(frame2,values=ListeEtablissement)    # Etablissement
	e6 = ttk.Combobox(frame2,values=ListeClasse)	  # Classe
	e66 = Entry(frame2)
	e7 = Entry(frame2)
	
	# frame3

	e8 = Entry(frame3)
	e9 = Entry(frame3)
	e10 = Entry(frame3)
	e11= Entry(frame3)
	e12= Entry(frame3)

	# frame4

	e13= Entry(frame4)
	e14= Entry(frame4)
	e15= Entry(frame4)
	
	#frame 5
	
	e16= Entry(frame5)
	e17= Entry(frame5)
	e18= Entry(frame5)

	ListeFoyer=[]
	with open ("foyer.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeFoyer.append(row)

	e19= ttk.Combobox(frame55,values=ListeFoyer)  # Foyer


	#___________________
	# frame 1
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e44.grid(row=4, column=1)
	e444.grid(row=5, column=1)
	e4444.grid(row=6, column=1)
	# frame 2
	e5.grid(row=0, column=1)
	e6.grid(row=1, column=1)
	e66.grid(row=2, column=1)
	e7.grid(row=3, column=1)

	# frame 3


	e8.grid(row=0, column=1)
	e9.grid(row=1, column=1)
	e10.grid(row=2, column=1)
	e11.grid(row=3, column=1)
	e12.grid(row=4, column=1)
	
	# frame 4
	
	e13.grid(row=0, column=1)  # Label Tuteur 1
	e14.grid(row=1, column=1) # Label Tuteur 2
	e15.grid(row=2, column=1)  # Label Tel Tuteur 1
	# frame 5
	e16.grid(row=0, column=1) # Label Tel Tuteur 2
	e17.grid(row=1, column=1)  # Label mail Tuteur 1
	e18.grid(row=2, column=1) # Label mail Tuteur 2

	e19.grid(row=0, column=1) # Label mail Tuteur 2
	
	#Button(fenetre1, text ='Editer').pack(side=RIGHT)
	#Button(fenetre1, text ='Sauver').pack(side=RIGHT)
	trimestre=["trimestre1", "trimestre2","trimestre3"]
	
	def ecriture():
		#file=str(e4444.get())+"/"+str(e5.get())+"/"+"inscription"+"/"
		file=str(e4444.get())+"/"+"inscription"+"/"

		try :
			os.makedirs(file)
			#os.path.join(file,"test.csv")
			#path=str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".csv"
			path=file+"inscription"+".csv"
			with open (path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e4444.get(),e5.get(),e6.get(),e66.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get()])
			
			with open ("inscription.csv",'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e4444.get(),e5.get(),e6.get(),e66.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get()])
			
			
			pdf = FPDF() 
		  
			# Add a page 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=30, h=30)
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Fiche d'inscription:",  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = "Année scolaire:"+str(e4444.get()),  
			         ln = 1, align = 'C') 

			pdf.cell(200, 10, txt = "Elève:"+" "+str(e2.get())+" "+str(e3.get())+" "+"N° Elève"+" "+str(e66.get()),  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			pdf.cell(200, 10, txt = "---Etat civil------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Civilité :" +str(e1.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Nom :" +str(e2.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Prenom :" +str(e3.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Date de Naissance :" +str(e4.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "NNI :" +str(e44.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Frai d'inscription :" +str(e444.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Année scolaire :" +str(e4444.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "------Scolarité-----", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Etablissement :" +str(e5.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Classe :" +str(e6.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "N° Elève :" +str(e66.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Adresse :" +str(e7.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Login :" +str(e8.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Mot de passe :" +str(e9.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Email :" +str(e11.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "N° Téléphone :" +str(e12.get()), ln = 2, align = 'l') 	
			pdf.cell(200, 10, txt = "-----Tuteur 1--------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tuteur 1:" +str(e13.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tel Tuteur 1:" +str(e14.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Email Tuteur 1:" +str(e15.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "-----Tuteur 2--------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tuteur 2:" +str(e16.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tel Tuteur 2:" +str(e17.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Email Tuteur 2:" +str(e18.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Foyer:" +str(e19.get()), ln = 2, align = 'l')


			  
			# save the pdf with name .pdf 
			fiche_eleve=str(e4444.get())+"/"+"inscription"+"/"+str(e44.get())+".pdf"
			pdf.output(fiche_eleve)
			
			#webbrowser.open_new(fiche_eleve)  
		except : 
			path=file+"inscription"+".csv"
			with open (path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e4444.get(),e5.get(),e6.get(),e66.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get()])
			
			with open ("inscription.csv",'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e4444.get(),e5.get(),e6.get(),e66.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get()])

			
			


			#anneeScolaire=str(e4444.get())+'/'
			#for i in trimestre :
			#file='Resultat/str(e4444.get())'
			#+os.path.join(str(e4444.get()))+'/'+os.path.join(str(e5.get()))+'/'+os.path.join(str(e6.get()))+'/'+os.path.join(str(e44.get()))+'/'+i
			#os.mkdir(file)
			# Add a page 
			pdf = FPDF() 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=30, h=30)
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Fiche d'inscription:",  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = "Année scolaire:"+str(e4444.get()),  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			pdf.cell(200, 10, txt = "---Etat civil------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Civilité :" +str(e1.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Nom :" +str(e2.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Prenom :" +str(e3.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Date de Naissance :" +str(e4.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "NNI :" +str(e44.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Frai d'inscription :" +str(e444.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Année scolaire :" +str(e4444.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "------Scolarité-----", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Etablissement :" +str(e5.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Classe :" +str(e6.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "N° Elève :" +str(e66.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Adresse :" +str(e7.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Login :" +str(e8.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Mot de passe :" +str(e9.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Email :" +str(e11.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "N° Téléphone :" +str(e12.get()), ln = 2, align = 'l') 	
			pdf.cell(200, 10, txt = "-----Tuteur 1--------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tuteur 1:" +str(e13.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tel Tuteur 1:" +str(e14.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Email Tuteur 1:" +str(e15.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "-----Tuteur 2--------", ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tuteur 2:" +str(e16.get()), ln = 2, align = 'l') 
			pdf.cell(200, 10, txt = "Tel Tuteur 2:" +str(e17.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Email Tuteur 2:" +str(e18.get()), ln = 2, align = 'l')
			pdf.cell(200, 10, txt = "Foyer:" +str(e19.get()), ln = 2, align = 'l')


			  
			# save the pdf with name .pdf 
			fiche_eleve=str(e4444.get())+"/"+"inscription"+"/"+str(e44.get())+".pdf"
			pdf.output(fiche_eleve)
			
			#webbrowser.open_new(fiche_eleve)  
		mb.showinfo("alerte", "Les informations ont bien été enregistrées")
	"""
	def Reset(): 

		e1.delete('1.0','end-1c')
		e2.delete('1.0','end-1c')
		e3.delete('1.0','end-1c')
		e4.delete('1.0','end-1c')
		e44.delete('1.0','end-1c')
		e444.delete('1.0','end-1c')
		e5.delete('1.0','end-1c')
		e6.delete('1.0','end-1c')
		e7.delete('1.0','end-1c')
		e8.delete('1.0','end-1c')
		e9.delete('1.0','end-1c')
		e10.delete('1.0','end-1c')
		e11.delete('1.0','end-1c')
		e12.delete('1.0','end-1c')
		e13.delete('1.0','end-1c')
		e14.delete('1.0','end-1c')
		e15.delete('1.0','end-1c')
		e16.delete('1.0','end-1c')
		e17.delete('1.0','end-1c')
		e18.delete('1.0','end-1c')
	"""
	def impression():
		# save FPDF() class into a  
		# variable pdf 
		pdf = FPDF() 
		  
		# Add a page 
		pdf.add_page() 
		  
		# set style and size of font  
		# that you want in the pdf 
		pdf.set_font("Arial", size = 15) 
		image="logo_awlama.png"
		pdf.image(image, w=30, h=30)
		  
		# create a cell 
		

		pdf.cell(200, 10, txt = "Fiche d'inscription:",  
		         ln = 1, align = 'C') 
		pdf.cell(200, 10, txt = "Année scolaire:"+" "+str(e3.get())+" "+str(e2.get())+" "+str(e4444.get()),  
		         ln = 1, align = 'C') 
		  
		# add another cell 
		pdf.cell(200, 10, txt = "---Etat civil------", ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Civilité :" +str(e1.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Nom :" +str(e2.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Prenom :" +str(e3.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Date de Naissance :" +str(e4.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "NNI :" +str(e44.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Frai d'inscription :" +str(e444.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Année scolaire :" +str(e4444.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "------Scolarité-----", ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Etablissement :" +str(e5.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Classe :" +str(e6.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "N° Elève :" +str(e66.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "Adresse :" +str(e7.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "Login :" +str(e8.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Mot de passe :" +str(e9.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Email :" +str(e11.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "N° Téléphone :" +str(e12.get()), ln = 2, align = 'l') 	
		pdf.cell(200, 10, txt = "-----Tuteur 1--------", ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Tuteur 1:" +str(e13.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Tel Tuteur 1:" +str(e14.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "Email Tuteur 1:" +str(e15.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "-----Tuteur 2--------", ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Tuteur 2:" +str(e16.get()), ln = 2, align = 'l') 
		pdf.cell(200, 10, txt = "Tel Tuteur 2:" +str(e17.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "Email Tuteur 2:" +str(e18.get()), ln = 2, align = 'l')
		pdf.cell(200, 10, txt = "Foyer:" +str(e19.get()), ln = 2, align = 'l')


		  
		# save the pdf with name .pdf 
		#fiche_eleve=str(e4444.get())+"/"+"inscription"+"/"+str(e44.get())+".pdf"
		pdf.output("fiche_eleve.pdf")
		
		webbrowser.open_new("fiche_eleve.pdf")  
	#Button(frame6, text ='imprimer',command=ecrire_pdf).grid(row=25,column=9)

	def list_inscrist():
		os.startfile("inscription.csv")

	

	Button(frame6, text ='Imprimer',command=impression).grid(row=0,column=0)
	Button(frame6, text ='Liste des inscrits',command=list_inscrist).grid(row=0,column=1)
	Button(frame6, text ='Sauver', command=ecriture).grid(row=0, column=2)
	#Button(frame55, text ='Ajouter foyer', command=Foyer).grid(row=0, column=2)
	#root.mainloop()


	
