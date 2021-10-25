# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb

def matiere(root):
	frame1 =LabelFrame(root, borderwidth=1)   # Liste des élèves
	frame1.grid(row=0, column=0, padx=10, pady=10)
	frame2 =LabelFrame(root, borderwidth=1)   
	frame2.grid(row=0, column=1, padx=10, pady=10)
	"""
	Label(root, text="Etablissement").grid(row=0)
	Label(root, text="Classe").grid(row=1)
	Label(root, text="Matière").grid(row=2)

	ListeEtablissement=["Ecole1", "Ecole2", "Ecole3"]
	ListeClasse=["Classe1", "Classe2", "Classe3"]
	#e1 = Entry(fenetre1)
	e1=ttk.Combobox(root,values=ListeEtablissement)
	e2 = ttk.Combobox(root,values=ListeClasse)
	e3 = Entry(root)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)

	
	"""
	liste=Listbox(frame1)
	a=[]
	with open ("matieres.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			a.append(row)
	valeur=int(len(a))
	for i in range(valeur):
		liste.insert(i,a[i])
	liste.pack()
	
	def ajouter():
		fen1=Toplevel()
		Label(fen1, text="Nouvelle Matière").grid(row=0)
		e1=Entry(fen1)
		e1.grid(row=0, column=1)
		def ecriture():
			with open ("matieres.csv",'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get()])
			
			mb.showinfo("alerte", "La matière"+" "+str(e1.get())+" "+"a bien été ajoutée")
		Button(fen1, text='Ajouter', command=ecriture).grid(row=1)

		fen1.title("Nouvelle Matière")
		fen1.geometry("300x300")
		fen1.configure(bg="orange")
		fen1.mainloop()

	Button(frame2, text ='Ajouter une matière',command=ajouter, bg='light green').grid(row=0,column=0)
	Button(frame2, text ='Sauver', bg='blue').grid(row=1,column=0)

	#mb.showinfo("alerte", "Les informations ont bien été enregistrées")


