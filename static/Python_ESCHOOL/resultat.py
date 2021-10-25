from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb
import os
import webbrowser
from fpdf import FPDF 

def Resultat(root):

	frame1 =LabelFrame(root, borderwidth=3)
	frame1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

	frame2=LabelFrame(root, borderwidth=3)
	frame2.grid(row=1, column=1,columnspan=2, padx=10, pady=10)

	frame3=LabelFrame(root, borderwidth=3)
	frame3.grid(row=2,column=0,columnspan=3, padx=10, pady=10)

	frame4=LabelFrame(root, borderwidth=3,relief=GROOVE)
	frame4.grid(row=3,column=2, padx=10, pady=10)

	Label(frame1, text="Année Scolaire").grid(row=0, column=0)
	Label(frame1, text="Etablissement").grid(row=0,column=2)
	Label(frame1, text="Classe").grid(row=1, column=0)
	Label(frame1, text="N° Elève").grid(row=1, column=2)

	Label(frame2, text="Trimestre").grid(row=0, column=0)

	#ListeClasse=["Classe1","Classe2", "Classe3"]
	#ListeEtablissement=["Ecole1","Ecole2", "Ecole3"]
	#ListeNNI_Eleve=["0089","67576", "688886"]
	ListeAnneeScolaire=["2020_2021","2021_2022", "2022_2023","2023_2024"]
	ListeTrimestre=["Trimestre1", "Trimestre2", "Trimestre3"]

	a=[]
	with open ("inscription.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			a.append(row)

	ListeNNI_Eleve=[]
	for i in range(int(len(a))) :
		ListeNNI_Eleve.append(a[i][:][4])

	Liste_Nom=[]
	for i in range(int(len(a))) :
		Liste_Nom.append(a[i][:][1])

	Liste_Prenom=[]
	for i in range(int(len(a))) :
		Liste_Prenom.append(a[i][:][2])

	Liste_NEleve=[]
	for i in range(int(len(a))) :
		Liste_NEleve.append(a[i][:][9])


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

	ListeMatiere=[]
	with open ("matieres.csv",'r', newline='')  as files :
		spamreader=csv.reader(files,delimiter=',',quotechar='|')
		#w.writerow([e1.get(),e2.get(),e3.get(),e4.get(),e44.get(),e444.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()])
		for row in spamreader :
			ListeMatiere.append(row)

	e1 = ttk.Combobox(frame1,values=ListeAnneeScolaire)
	e2 = ttk.Combobox(frame1,values=ListeEtablissement)
	e3 = ttk.Combobox(frame1,values=ListeClasse)	
	e4 = ttk.Combobox(frame1,values=Liste_NEleve)

	e5 = ttk.Combobox(frame2,values=ListeTrimestre)

	e1.grid(row=0, column=1)
	e2.grid(row=0, column=3)
	e3.grid(row=1, column=1)
	e4.grid(row=1, column=3)

	e5.grid(row=0, column=1)

	#import test_vecteur_resultat.tableau as tb

	#tb(frame3)
	e=Entry(frame3)
	e.configure(state=DISABLED)

	#ligne0, 
	e00=Entry(frame3)
	e00.insert(0,"Note 1")
	e00.configure(bg='blue',fg='white')
	e01=Entry(frame3)
	e01.insert(0,"Note 2")
	e01.configure(bg='blue',fg='white')
	e02=Entry(frame3)
	e02.insert(0,"Note 3")
	e02.configure(bg='blue',fg='white')
	e03=Entry(frame3)
	e03.insert(0,"Note 4")
	e03.configure(bg='blue',fg='white')
	e04=Entry(frame3)
	e04.insert(0,"Note 5")
	e04.configure(bg='blue',fg='white')


	#ligne0, 
	e10=ttk.Combobox(frame3, values=ListeMatiere)
	#e10.configure(bg='orange')
	e11=Entry(frame3)
	e12=Entry(frame3)
	e13=Entry(frame3)
	e14=Entry(frame3)
	e15=Entry(frame3)

	#ligne0, 
	e20=ttk.Combobox(frame3, values=ListeMatiere)
	#e20.configure(bg='orange')
	e21=Entry(frame3)
	e22=Entry(frame3)
	e23=Entry(frame3)
	e24=Entry(frame3)
	e25=Entry(frame3)

	#ligne0, 
	e30=ttk.Combobox(frame3, values=ListeMatiere)
	#e30.configure(bg='orange')
	e31=Entry(frame3)
	e32=Entry(frame3)
	e33=Entry(frame3)
	e34=Entry(frame3)
	e35=Entry(frame3)

	#ligne0, 
	e40=ttk.Combobox(frame3, values=ListeMatiere)
	#e40.configure(bg='orange')
	e41=Entry(frame3)
	e42=Entry(frame3)
	e43=Entry(frame3)
	e44=Entry(frame3)
	e45=Entry(frame3)

	#ligne0, 
	e50=ttk.Combobox(frame3, values=ListeMatiere)
	#e50.configure(bg='orange')
	e51=Entry(frame3)
	e52=Entry(frame3)
	e53=Entry(frame3)
	e54=Entry(frame3)
	e55=Entry(frame3)

	#ligne0, 
	e60=ttk.Combobox(frame3, values=ListeMatiere)
	#e60.configure(bg='orange')
	e61=Entry(frame3)
	e62=Entry(frame3)
	e63=Entry(frame3)
	e64=Entry(frame3)
	e65=Entry(frame3)

	#ligne0, 
	e70=ttk.Combobox(frame3, values=ListeMatiere)
	#e70.configure(bg='orange')
	e71=Entry(frame3)
	e72=Entry(frame3)
	e73=Entry(frame3)
	e74=Entry(frame3)
	e75=Entry(frame3)

	#ligne0, 
	e80=ttk.Combobox(frame3, values=ListeMatiere)
	#e80.configure(bg='orange')
	e81=Entry(frame3)
	e82=Entry(frame3)
	e83=Entry(frame3)
	e84=Entry(frame3)
	e85=Entry(frame3)

	#ligne0, 
	e90=ttk.Combobox(frame3, values=ListeMatiere)
	#e90.configure(bg='orange')
	e91=Entry(frame3)
	e92=Entry(frame3)
	e93=Entry(frame3)
	e94=Entry(frame3)
	e95=Entry(frame3)

	#ligne0, 
	e100=ttk.Combobox(frame3, values=ListeMatiere)
	#e100.configure(bg='orange')
	e101=Entry(frame3)
	e102=Entry(frame3)
	e103=Entry(frame3)
	e104=Entry(frame3)
	e105=Entry(frame3)

	e.grid(row=0, column=0)

	e00.grid(row=0,column=1)
	e01.grid(row=0,column=2)
	e02.grid(row=0,column=3)
	e03.grid(row=0,column=4)
	e04.grid(row=0,column=5)

	e10.grid(row=1,column=0)
	e11.grid(row=1,column=1)
	e12.grid(row=1,column=2)
	e13.grid(row=1,column=3)
	e14.grid(row=1,column=4)
	e15.grid(row=1,column=5)

	e20.grid(row=2,column=0)
	e21.grid(row=2,column=1)
	e22.grid(row=2,column=2)
	e23.grid(row=2,column=3)
	e24.grid(row=2,column=4)
	e25.grid(row=2,column=5)

	e30.grid(row=3,column=0)
	e31.grid(row=3,column=1)
	e32.grid(row=3,column=2)
	e33.grid(row=3,column=3)
	e34.grid(row=3,column=4)
	e35.grid(row=3,column=5)

	e40.grid(row=4,column=0)
	e41.grid(row=4,column=1)
	e42.grid(row=4,column=2)
	e43.grid(row=4,column=3)
	e44.grid(row=4,column=4)
	e45.grid(row=4,column=5)

	e50.grid(row=5,column=0)
	e51.grid(row=5,column=1)
	e52.grid(row=5,column=2)
	e53.grid(row=5,column=3)
	e54.grid(row=5,column=4)
	e55.grid(row=5,column=5)

	e60.grid(row=6,column=0)
	e61.grid(row=6,column=1)
	e62.grid(row=6,column=2)
	e63.grid(row=6,column=3)
	e64.grid(row=6,column=4)
	e65.grid(row=6,column=5)

	e70.grid(row=7,column=0)
	e71.grid(row=7,column=1)
	e72.grid(row=7,column=2)
	e73.grid(row=7,column=3)
	e74.grid(row=7,column=4)
	e75.grid(row=7,column=5)

	e80.grid(row=8,column=0)
	e81.grid(row=8,column=1)
	e82.grid(row=8,column=2)
	e83.grid(row=8,column=3)
	e84.grid(row=8,column=4)
	e85.grid(row=8,column=5)

	e90.grid(row=9,column=0)
	e91.grid(row=9,column=1)
	e92.grid(row=9,column=2)
	e93.grid(row=9,column=3)
	e94.grid(row=9,column=4)
	e95.grid(row=9,column=5)

	e100.grid(row=10,column=0)
	e101.grid(row=10,column=1)
	e102.grid(row=10,column=2)
	e103.grid(row=10,column=3)
	e104.grid(row=10,column=4)
	e105.grid(row=10,column=5)

	

	ligne0=[e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get()]
	ligne1=[e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get()]
	ligne2=[e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()]
	ligne3=[e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get()]
	ligne4=[e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get()]
	ligne5=[e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get()]
	ligne6=[e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get()]
	ligne7=[e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get()]
	ligne8=[e80.get(),e81.get(),e82.get(),e83.get(),e84.get(),e85.get()]
	ligne9=[e90.get(),e91.get(),e92.get(),e93.get(),e94.get(),e95.get()]
	ligne10=[e100.get(),e101.get(),e102.get(),e103.get(),e104.get(),e105.get()]

	data=[ligne0,ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10]

	def ecriture():

		ligne0=[e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get()]
		ligne1=[e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get()]
		ligne2=[e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()]
		ligne3=[e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get()]
		ligne4=[e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get()]
		ligne5=[e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get()]
		ligne6=[e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get()]
		ligne7=[e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get()]
		ligne8=[e80.get(),e81.get(),e82.get(),e83.get(),e84.get(),e85.get()]
		ligne9=[e90.get(),e91.get(),e92.get(),e93.get(),e94.get(),e95.get()]
		ligne10=[e100.get(),e101.get(),e102.get(),e103.get(),e104.get(),e105.get()]

		data=[ligne0,ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10]
		

		file=str(e1.get())+"/"+"Resultat"+"/"+str(e2.get())+"/"+str(e3.get())+"/"+str(e5.get())+"/"+str(e4.get())+"/"
		try :
			os.makedirs(file)
			#os.path.join(file,"test.csv")
			path=str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".csv"

			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get()])
				w.writerow([e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get()])
				w.writerow([e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()])
				w.writerow([e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get()])
				w.writerow([e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get()])
				w.writerow([e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get()])
				w.writerow([e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get()])
				w.writerow([e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get()])
				w.writerow([e80.get(),e81.get(),e82.get(),e83.get(),e84.get(),e85.get()])
				w.writerow([e90.get(),e91.get(),e92.get(),e93.get(),e94.get(),e95.get()])
				w.writerow([e100.get(),e101.get(),e102.get(),e103.get(),e104.get(),e105.get()])

			pdf = FPDF(orientation = 'L', unit = 'mm', format='A4') 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=30, h=30)
			epw = pdf.w - 2*pdf.l_margin
 
			# Set column width to 1/4 of effective page width to distribute content 
			# evenly across table and page
			col_width = epw/6
			# Text height is the same as current font size
			th = pdf.font_size
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Resultat:"+" "+str(e5.get()),  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt ="Année scoalaire:"+" "+str(e1.get())+" "+"Classe:"+" "+str(e3.get())+" "+"N° Elève:"+" "+str(e4.get()),  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = "N° Elève:"+" "+str(e4.get()),  
			         ln = 1, align = 'C') 

			for row in data:
			    for datum in row:
			        # Enter data in colums
			        # Notice the use of the function str to coerce any input to the 
			        # string type. This is needed
			        # since pyFPDF expects a string, not a number.
			        pdf.cell(col_width, th, str(datum), border=1)
			 
			    pdf.ln(th)

			pdf.cell(200, 10, txt = "Le directeur",  
			         ln = 1, align = 'r') 

			  
			# save the pdf with name .pdf 
			fiche_resultat=file+str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".pdf"
			pdf.output(fiche_resultat)
		except :

			path=str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".csv"

			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get()])
				w.writerow([e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get()])
				w.writerow([e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()])
				w.writerow([e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get()])
				w.writerow([e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get()])
				w.writerow([e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get()])
				w.writerow([e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get()])
				w.writerow([e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get()])
				w.writerow([e80.get(),e81.get(),e82.get(),e83.get(),e84.get(),e85.get()])
				w.writerow([e90.get(),e91.get(),e92.get(),e93.get(),e94.get(),e95.get()])
				w.writerow([e100.get(),e101.get(),e102.get(),e103.get(),e104.get(),e105.get()])

			pdf = FPDF(orientation = 'L', unit = 'mm', format='A4') 
			pdf.add_page() 
			  
			# set style and size of font  
			# that you want in the pdf 
			pdf.set_font("Arial", size = 15) 
			image="logo_awlama.png"
			pdf.image(image, w=30, h=30)
			epw = pdf.w - 2*pdf.l_margin
 
			# Set column width to 1/4 of effective page width to distribute content 
			# evenly across table and page
			col_width = epw/6
			# Text height is the same as current font size
			th = pdf.font_size
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Resultat:"+" "+str(e5.get()),  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt ="Année scoalaire:"+" "+str(e1.get())+" "+"Classe:"+" "+str(e3.get())+" "+"N° Elève:"+" "+str(e4.get()),  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = "N° Elève:"+" "+str(e4.get()),  
			         ln = 1, align = 'C') 

			for row in data:
			    for datum in row:
			        # Enter data in colums
			        # Notice the use of the function str to coerce any input to the 
			        # string type. This is needed
			        # since pyFPDF expects a string, not a number.
			        pdf.cell(col_width, th, str(datum), border=1)
			 
			    pdf.ln(th)

			pdf.cell(200, 10, txt = "Le directeur",  
			         ln = 1, align = 'r') 

			  
			# save the pdf with name .pdf 
			fiche_resultat=file+str(e1.get())+"_"+"resultat"+"_"+str(e3.get())+"_"+str(e5.get())+"_"+str(e4.get())+".pdf"
			pdf.output(fiche_resultat)

		
		mb.showinfo("alerte", "Les informations ont bien été enregistrées")


	def impression():
		ligne0=[e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get()]
		ligne1=[e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get()]
		ligne2=[e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()]
		ligne3=[e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get()]
		ligne4=[e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get()]
		ligne5=[e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get()]
		ligne6=[e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get()]
		ligne7=[e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get()]
		ligne8=[e80.get(),e81.get(),e82.get(),e83.get(),e84.get(),e85.get()]
		ligne9=[e90.get(),e91.get(),e92.get(),e93.get(),e94.get(),e95.get()]
		ligne10=[e100.get(),e101.get(),e102.get(),e103.get(),e104.get(),e105.get()]

		data=[ligne0,ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10]

		pdf = FPDF(orientation = 'L', unit = 'mm', format='A4') 
		pdf.add_page() 
		  
		# set style and size of font  
		# that you want in the pdf 
		pdf.set_font("Arial", size = 15) 
		image="logo_awlama.png"
		pdf.image(image, w=30, h=30)
		epw = pdf.w - 2*pdf.l_margin

		# Set column width to 1/4 of effective page width to distribute content 
		# evenly across table and page
		col_width = epw/6
		# Text height is the same as current font size
		th = pdf.font_size
		  
		# create a cell 
		

		pdf.cell(200, 10, txt = "Resultat:"+" "+str(e5.get()),  
			         ln = 1, align = 'C') 
		pdf.cell(200, 10, txt ="Année scoalaire:"+" "+str(e1.get())+" "+"Classe:"+" "+str(e3.get())+" "+"N° Elève:"+" "+str(e4.get()),  
		         ln = 1, align = 'C') 
		pdf.cell(200, 10, txt = "N° Elève:"+" "+str(e4.get()),  
		         ln = 1, align = 'C') 

		for row in data:
		    for datum in row:
		        # Enter data in colums
		        # Notice the use of the function str to coerce any input to the 
		        # string type. This is needed
		        # since pyFPDF expects a string, not a number.
		        pdf.cell(col_width, th, str(datum), border=1)
		 
		    pdf.ln(th)

		pdf.cell(200, 10, txt = "Le directeur",  
			         ln = 1, align = 'r') 

		  
		# save the pdf with name .pdf 
		fiche_resultat="resultat.pdf"
		pdf.output(fiche_resultat)
		webbrowser.open_new(fiche_resultat)





	
	Button(frame4, text ='Imprimer',command=impression).grid(row=0,column=0)
	Button(frame4, text ='Sauver', command=ecriture).grid(row=0,column=1)


