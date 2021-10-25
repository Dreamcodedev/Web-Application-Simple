# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb

def Etablissements(root):
	

	Label(root, text="Etablissement").grid(row=0)
	Label(root, text="Adresse").grid(row=1)
	Label(root, text="Directeur Etablissement").grid(row=2)
	Label(root, text="E-mail").grid(row=3)
	Label(root, text="Tel").grid(row=4)

	e1 = Entry(root)
	e2 = Entry(root)
	e3 = Entry(root)
	e4 = Entry(root)
	e5 = Entry(root)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1)

	def ecriture():
			with open ("etablissement.csv",'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e5.get()])
			mb.showinfo("alerte", "LEtbalissement"+" "+str(e1.get())+" "+"a bien été ajouté")

	Button(root, text ='Editer').grid(row=25,column=8)
	Button(root, text ='Sauver', command=ecriture).grid(row=25,column=9)
	
	
