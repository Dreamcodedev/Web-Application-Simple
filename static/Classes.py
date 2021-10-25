# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb

def classe(root):

	

	Label(root, text="Etablissement").grid(row=0)
	Label(root, text="Classe").grid(row=1)
	Label(root, text="Catégorie").grid(row=2)

	a=[]
	with open ("etablissement.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			a.append(row)
	#ListeEtablissement=["Ecole1", "Ecole2", "Ecole3"]"1ere année primaire",

	#b=a[1:]
	Categorie_Classe=["CP1","CP2","CE1","CE2",
	"CM1","CM2","1ère année collège","2ème année collège","3ème année collège",
	"4ème année collège","5ème année collège","6ème année collège","Terminale","Licence 1","Licence 2",
	"Licence 3","Master 1","Master 2","PHD","BT","BTS","Maternelle"]
	
	b=[]
	for i in range(int(len(a))) :
		b.append(a[i][:][0])

	e1=ttk.Combobox(root,values=b[1:])
	e2 = Entry(root)
	e3=ttk.Combobox(root,values=Categorie_Classe)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)	
	
	
	def ecriture():
		

		with open ("classe.csv",'a', newline='')  as files :
			w=csv.writer(files,delimiter=',',lineterminator='\n')
			w.writerow([e1.get(),e2.get(),e3.get()])
		mb.showinfo("alerte", "La classe"+" "+str(e2.get())+" "+"pour établissement"+" "+str(e1.get())+" "+"a bien été ajoutée")
	#Button(root, text ='Editer').grid(row=25,column=8)
	Button(root, text ='Sauver', command=ecriture).grid(row=25,column=9)
	


