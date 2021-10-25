# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import os
import csv
from fpdf import FPDF 
import webbrowser

def Foyer(root):
	Label(root, text="Foyer").grid(row=0,column=0)
	e1=Entry(root)
	e1.grid(row=0,column=1)

	def ecrire():

		with open ("foyer.csv",'a', newline='')  as files :
			w=csv.writer(files,delimiter=',',lineterminator='\n')
			w.writerow([e1.get()])

		mb.showinfo("alerte", "Les informations ont bien été enregistrées")

	Button(root, text ='Sauver', command=ecrire).grid(row=0, column=2)

