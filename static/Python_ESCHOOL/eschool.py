# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
import csv
import os
from tkinter import messagebox as mb

fenetre = Toplevel()
fenetre.title("Jënd E-school")
fenetre.configure(bg='orange')

"""
heading = Label(text="Bienvenue dans votre application E-SCHOOL",bg="yellow",fg="black",font="10")
heading.pack()
"""
logo = PhotoImage(file="logo_awlama.png")

w1 = Label(fenetre, image=logo, bg='orange').pack()

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre, borderwidth=3, background="blue",foreground="white",
               activebackground="green")

"""
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)
"""
#==================== Administration ======================
def Administration():
	fenetre=Toplevel()
	fenetre.title("Administration")
	fenetre.configure(bg="light blue")
	from dashboard import table_bord
	table_bord(fenetre)
	fenetre.mainloop()

	
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Administration", command=Administration)
menubar.add_cascade(label="Dashboard", menu=menu1)


# =================Menu inscription==============
def Inscription():
	#fenetre1=Tk()
	
	#a=inscription(fenetre1)
	fenetre=Toplevel()
	fenetre.title("Inscription")
	fenetre.configure(bg="light blue")
	from inscription import Inscription
	Inscription(fenetre)
	fenetre.mainloop()
	

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Inscription", command=Inscription)
menubar.add_cascade(label="Inscription", menu=menu2)

#============ Menu Matière ========================================

def matieres():
	
	fenetre= Toplevel()
	fenetre.title("Gestion des Matieres")
	fenetre.geometry("500x500")
	fenetre.configure(bg="light blue")
	from Matiere import matiere
	matiere(fenetre)
	fenetre.mainloop()
		
	

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Matières", command=matieres)
menubar.add_cascade(label="Matières", menu=menu3)

#========================= Menu classe====================

def classe():
	
	fenetre3= Toplevel()
	fenetre3.title("Gestion des Classes")
	fenetre3.geometry("500x500")
	fenetre3.configure(bg="light blue")
	from Classes import classe
	classe(fenetre3)
	fenetre3.mainloop()

menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="Classes", command=classe)
menubar.add_cascade(label="Classes", menu=menu4)

#============= Menu Etablissement =============

def etablissement():
	
	fenetre4= Toplevel()
	fenetre4.title("Gestion des établissements")
	fenetre4.geometry("500x500")
	fenetre4.configure(bg='light blue')
	from etablissement import Etablissements
	Etablissements(fenetre4)
	fenetre4.mainloop()
	

menu5 = Menu(menubar, tearoff=0)
menu5.add_command(label="Etablissement", command=etablissement)
menubar.add_cascade(label="Etablissement", menu=menu5)


#===================== Gestion des éleves ================

def eleves():
	fenetre5= Toplevel()
	fenetre5.title("Gestion des élèves")
	#fenetre5.geometry("500x500")
	fenetre5.configure(bg="light blue")
	from eleves import Eleves
	Eleves(fenetre5)
	fenetre5.mainloop()

	
	
menu6 = Menu(menubar, tearoff=0)
menu6.add_command(label="Elèves", command=eleves)
menubar.add_cascade(label="Elèves", menu=menu6)

#========================== Menu professeur ==============
def professeur():	
	
	fenetre6= Tk()
	fenetre6.title("Gestion des professeurs")
	#fenetre6.geometry("800x900")
	fenetre6.configure(bg='light blue')
	from professeur import Professeurs
	Professeurs(fenetre6)
	fenetre6.mainloop()
	


menu7 = Menu(menubar, tearoff=0)
menu7.add_command(label="Professeurs", command=professeur)
menubar.add_cascade(label="Professeurs", menu=menu7)


#===================== Gestion des emploi du temps================

def emploi_temps() :

	
	fenetre7= Toplevel()
	fenetre7.title("Gestion des emplois du temps")
	#fenetre7.geometry("800x800")
	from time_table import Emploi_temps
	Emploi_temps(fenetre7)
	fenetre7.configure(bg='light blue')
	fenetre7.mainloop()
	

		
menu8 = Menu(menubar, tearoff=0)
menu8.add_command(label="Emploi du temps", command=emploi_temps)
menubar.add_cascade(label="Emploi du temps", menu=menu8)


#====================== Message ===================
import smtplib
#from mail import send_message

def email():
	
	#app = Toplevel()

	#app.geometry("500x500")

	#app.title("E-Mail")
	
	window=Tk()
	window.title('Email Client')
	window.geometry('500x500')
	window.configure(bg='light blue')
	from message import Message
	Message(window)
	window.mainloop()
	"""
	
	#frame1 =LabelFrame(app, borderwidth=3)
	#frame1.grid(row=10, column=1, padx=10, pady=10)
	
	#frame2 =LabelFrame(app, borderwidth=3)
	#frame2.grid(row=0, column=0, padx=10, pady=10)
	
	heading = Label(app,text="Envoyez votre message",bg="yellow",fg="black",font="10")

	heading.grid(row=0,column=0)
	
	address_field = Label(app,text="Recipient Address :")
	email_body_field = Label(app,text="Message :")

	address_field.grid(row=1,column=0)
	email_body_field.grid(row=2,column=0)

	address = StringVar()
	email_body = StringVar()


	address_entry = Entry(app,textvariable=address,width="30")
	email_body_entry = Entry(app,textvariable=email_body,width="30")

	address_entry.grid(row=1,column=2)
	email_body_entry.grid(row=2,column=2)

	button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="grey")

	button.grid(row=3, column=2)

	"""
	#app.mainloop()
	
	
	
menu9 = Menu(menubar, tearoff=0)
menu9.add_command(label="Message", command=email)
menubar.add_cascade(label="Message", menu=menu9)
#===========================Resultat======================

def result() :

	
	fenetre9= Toplevel()
	fenetre9.title("Gestion des resultats")
	fenetre9.configure(bg="light green")
	from resultat import Resultat
	Resultat(fenetre9)
	fenetre9.mainloop()

menu10 = Menu(menubar, tearoff=0)
menu10.add_command(label="Resultat", command=result)
menubar.add_cascade(label="Resultat", menu=menu10)
#================================== Situation comptable=============

def Comptable():
	
	fenetre10= Toplevel()
	fenetre10.title("Situation comptable")
	fenetre10.configure(bg="light green")
	from situation_comptable import Situation_Comptable
	Situation_Comptable(fenetre10)
	fenetre10.mainloop()

menu11 = Menu(menubar, tearoff=0)
menu11.add_command(label="Comptabilite", command=Comptable)
menubar.add_cascade(label="Situation comptable", menu=menu11)

def Foyer():
		windows=Toplevel()
		from foyer import Foyer
		Foyer(windows)
		windows.mainloop()

menu12 = Menu(menubar, tearoff=0)
#menu12.add_command(label="Compte", command=Newfenetre)
menu12.add_command(label="Foyer", command=Foyer)
menubar.add_cascade(label="Foyer", menu=menu12)


#==========================

def quitter():
	fenetre.quit()
	#fenetre.destroy()

#========================  Compte=======
menu13 = Menu(menubar, tearoff=0)
#menu12.add_command(label="Compte", command=Newfenetre)
menu13.add_command(label="Quitter", command=quitter)
menubar.add_cascade(label="Compte", menu=menu13)


#Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)



fenetre.config(menu=menubar)
fenetre.mainloop()
