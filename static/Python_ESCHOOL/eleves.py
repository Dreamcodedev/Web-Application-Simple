# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb
from fpdf import FPDF 
import webbrowser

def Eleves(root):

	

	frame1 =LabelFrame(root, borderwidth=3)   # Liste des élèves
	frame1.grid(row=10, column=1, padx=10, pady=10)

	frame11 =LabelFrame(root, borderwidth=3)   # Absence
	frame11.grid(row=10, column=2, padx=10, pady=10)

	frame2 =LabelFrame(root, borderwidth=3)  # Champs nom, prénom, année de naissance, classe
	frame2.grid(row=11, column=1, padx=10, pady=10)

	frame3 =LabelFrame(root, borderwidth=3) #  Champs adresse, contact, E-mail
	frame3.grid(row=12, column=1, padx=10, pady=10)

	frame4 =LabelFrame(root, borderwidth=3)  # Champs tuteur, tel tuteur, e-mail tuteur
	frame4.grid(row=11, column=2, padx=10, pady=10)
	#photo = PhotoImage(file="logo1.png")
	frame5 =LabelFrame(root, borderwidth=3, width=20, height=20)    # Champs photo élève
	frame5.grid(row=10, column=3, padx=10, pady=10)

	frame6 =LabelFrame(root, borderwidth=3)         # Champs bouton- sauver
	frame6.grid(row=19, column=3, padx=10, pady=10)

	#from PIL import Image
	"""
	File="logo1.png"
	photo = Image.open(File)
	# conversion de l'image
	photo.save("logo1.gif")
	
	Photo_Eleve= PhotoImage(file="logo2.png")
	canvas=Canvas(frame5, width=50, height=50)

	#w1 = Label(canvas, image=photo).pack()
	#canvas.grid(row=0, column=0)
	#canvas=Canvas(frame5, width=100, height=120)
	
	canvas.create_image(30,30, image=Photo_Eleve)
	canvas.pack()
	#canvas.grid(row=0, column=0)
	"""
	Label(frame1, text="Année scolaire").grid(row=0, column=0)
	Label(frame1, text="Classe").grid(row=0, column=2)
	Label(frame1, text="Numéro élève").grid(row=0, column=4)
	

	Label(frame2, text="Nom").grid(row=1)
	Label(frame2, text="Prénom").grid(row=2)
	Label(frame2, text="Date de naissance").grid(row=3)
	Label(frame2, text="Classe").grid(row=4)

	Label(frame3, text="Adresse").grid(row=6)
	Label(frame3, text="Contact").grid(row=7)
	Label(frame3, text="E-Mail").grid(row=8)


	Label(frame4, text="Tuteur").grid(row=0, column=5)
	Label(frame4, text="Tel Tuteur").grid(row=1, column=5)
	Label(frame4, text="E-Mail Tuteur").grid(row=2, column=5)

	#ListeEleves=["Fatimetou", "Amina", "Halima", "Mohammed"]
	#ListeClasse=["Classe1","Classe2", "Classe3"]

	a=[]
	with open ("inscription.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			a.append(row)
	#ListeEtablissement=["Ecole1", "Ecole2", "Ecole3"]
	#b=a[1:]
	Liste_NEleve=[]
	for i in range(int(len(a))) :
		Liste_NEleve.append(a[i][:][9])

	ListeEleves_Nom=[]
	for i in range(int(len(a))) :
		ListeEleves_Nom.append(a[i][:][1])

	ListeEleves_Prenom=[]
	for i in range(int(len(a))) :
		ListeEleves_Prenom.append(a[i][:][2])
	
	ListeEleves_DateNaissance=[]
	for i in range(int(len(a))) :
		ListeEleves_DateNaissance.append(a[i][:][3])

	ListeEleves_AScolaire=[]
	for i in range(int(len(a))) :
		ListeEleves_AScolaire.append(a[i][:][6])
	
	ListeEleves_Classe=[]
	for i in range(int(len(a))) :
		ListeEleves_Classe.append(a[i][:][8])

	
	ListeClasse_b=[]
	with open ("classe.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeClasse_b.append(row)

	ListeClasse=[]
	for i in range(int(len(ListeClasse_b))) :
		ListeClasse.append(ListeClasse_b[i][:][1])
	

	ListeEleves_Adresse=[]
	for i in range(int(len(a))) :
		ListeEleves_Adresse.append(a[i][:][10])

	ListeEleves_Contact=[]
	for i in range(int(len(a))) :
		ListeEleves_Contact.append(a[i][:][15])

	ListeEleves_Email=[]
	for i in range(int(len(a))) :
		ListeEleves_Email.append(a[i][:][14])

	ListeEleves_Tuteur=[]
	for i in range(int(len(a))) :
		ListeEleves_Tuteur.append(a[i][:][16])

	ListeEleves_Tuteur_Contact=[]
	for i in range(int(len(a))) :
		ListeEleves_Tuteur_Contact.append(a[i][:][17])

	ListeEleves_Tuteur_Email=[]
	for i in range(int(len(a))) :
		ListeEleves_Tuteur_Email.append(a[i][:][18])

	AScolaire=["2020_2021","2021_2022","2022_2023","2023_2024","2024_2025"]
	#e1 = ttk.Combobox(frame1,values=Liste_NNI)
	#e1.current(5)
	e1=ttk.Combobox(frame1,values=AScolaire)
	e111=ttk.Combobox(frame1, values=ListeClasse)
	e1111=Entry(frame1)
	#e22=StringVar()



	#e2 = Entry(frame2, textvariable=e22)
	e2 = Entry(frame2)
	e2.configure(state=DISABLED)
			
	e3 = Entry(frame2)
	e3.configure(state=DISABLED)

	e4 = Entry(frame2)
	e4.configure(state=DISABLED)
	#e5 = ttk.Combobox(frame2,values=ListeEleves_Classe)
	e5=Entry(frame2)
	e5.configure(state=DISABLED)

	e6 = Entry(frame3)
	e6.configure(state=DISABLED)

	e7 = Entry(frame3)
	e7.configure(state=DISABLED)

	e8 = Entry(frame3)
	e8.configure(state=DISABLED)

	e9 = Entry(frame4)
	e9.configure(state=DISABLED)

	e10 = Entry(frame4)	
	e10.configure(state=DISABLED)

	e11 = Entry(frame4)
	e11.configure(state=DISABLED)

	def affichage():
		for i in range(int(len(Liste_NEleve))):
			#for j in range(int(len(ListeClasse))):

			if e1.get()==ListeEleves_AScolaire[i] and e111.get()==ListeEleves_Classe[i] and e1111.get()==Liste_NEleve[i] :
				e2.delete(0,END)
				e2.insert(0,ListeEleves_Nom[i])
				e3.delete(0,END)
				e3.insert(0,ListeEleves_Prenom[i])
				e4.delete(0,END)
				e4.insert(0,ListeEleves_DateNaissance[i])
				e5.delete(0,END)
				e5.insert(0,ListeEleves_Classe[i])
				e6.delete(0,END)
				e6.insert(0,ListeEleves_Adresse[i])
				e7.delete(0,END)
				e7.insert(0,ListeEleves_Contact[i])
				e8.delete(0,END)
				e8.insert(0,ListeEleves_Email[i])
				e9.delete(0,END)
				e9.insert(0,ListeEleves_Tuteur[i])
				e10.delete(0,END)
				e10.insert(0,ListeEleves_Tuteur_Contact[i])
				e11.delete(0,END)
				e11.insert(0,ListeEleves_Tuteur_Email[i])

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
					pdf.image(image, w=30, h=30)
					  
					# create a cell 
					

					pdf.cell(200, 10, txt = "Fichier d'information de l'élèves :" +str(e2.get())+" "+str(e3.get()),  
					         ln = 1, align = 'C') 
					  
					# add another cell 
					pdf.cell(200, 10, txt = "N° Elève :" +str(e1111.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Nom :" +str(e2.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Prenom :" +str(e3.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Date de Naissance :" +str(e4.get()), ln = 2, align = 'l') 
					#pdf.cell(200, 10, txt = "Etablissement :" +str(e5.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Classe :" +str(e5.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Adresse :" +str(e7.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Email :" +str(e8.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Tuteur :" +str(e9.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Contact Tuteur :" +str(e10.get()), ln = 2, align = 'l') 
					pdf.cell(200, 10, txt = "Email Tuteur :" +str(e11.get()), ln = 2, align = 'l') 
					  
					  
					# save the pdf with name .pdf 
					pdf.output("eleves.pdf")
					
					webbrowser.open_new("eleves.pdf")  
				Button(frame6, text ='imprimer',command=ecrire_pdf).grid(row=25,column=9)


	def edition():
		#objet_entry.configure(state=etat)
		e2.configure(state=NORMAL)
		e3.configure(state=NORMAL)
		e4.configure(state=NORMAL)
		e5.configure(state=NORMAL)
		e6.configure(state=NORMAL)
		e7.configure(state=NORMAL)
		e8.configure(state=NORMAL)
		e9.configure(state=NORMAL)
		e10.configure(state=NORMAL)
		e11.configure(state=NORMAL)
		#e2.configure(state=DISABLED)


				#e22.set(ListeEleves_Prenom[i])

	def Absence():
		fenetre=Toplevel()
		fenetre.title("Absence")
		fenetre.configure(bg="light green")
		from Absences import absences
		absences(fenetre)
		fenetre.mainloop()

	e1.grid(row=0, column=1)
	e111.grid(row=0, column=3)
	e1111.grid(row=0, column=5)
	#------------------
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1)

	e6.grid(row=6, column=1)
	e7.grid(row=7, column=1)
	e8.grid(row=8, column=1)

	e9.grid(row=0, column=6)
	e10.grid(row=1, column=6)
	e11.grid(row=2, column=6)

	Button(frame6, text ='Editer', command=edition).grid(row=25,column=8)
	
	Button(frame1, text ='OK', command=affichage).grid(row=0,column=6)

	Button(frame11, text ='Saisie Absence', command=Absence).grid(row=0,column=1)
	
"""	

fenetre5= Tk()
fenetre5.title("Gestion des élèves")
fenetre5.geometry("800x800")
fenetre5.configure(bg="light blue")
Eleves(fenetre5)
#fenetre5.after(1000,fenetre5)
fenetre5.mainloop()
"""