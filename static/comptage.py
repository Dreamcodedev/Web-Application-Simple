# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb

def csvcount(filename): # pour le comptage des lignes
    with open(filename, 'r') as f:
        i = 0
        for ligne in f:
            i += 1
    return i

def chaine(filename, chaine):   # pour le compatage d'un mot sur les lignes
	#chaine = "coucou" # Texte à rechercher
	with open(filename,'r') as f:
		i=0
		for ligne in f:
		    if chaine in ligne:
		        i+=1
	return i

	
