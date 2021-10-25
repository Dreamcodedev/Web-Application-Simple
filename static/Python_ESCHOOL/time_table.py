# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import sys
import csv
from tkinter import messagebox as mb
import os
from fpdf import FPDF 
import webbrowser

def Emploi_temps(root):

	frame1 =LabelFrame(root, borderwidth=3)
	frame1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


	frame2=LabelFrame(root, borderwidth=3)
	frame2.grid(row=1,column=0,columnspan=3, padx=10, pady=10)

	frame3=LabelFrame(root, borderwidth=3)
	frame3.grid(row=2, column=0, padx=10, pady=10)
	"""
	Label(fenetre7, text="Classe").grid(row=0)
	Label(fenetre7, text="Etablissement").grid(row=1)

	ListeClasse=["Classe1","Classe2", "Classe3"]
	ListeEtablissement=["Ecole1","Ecole2", "Ecole3"]	
	"""
	Label(frame1, text="Année Scolaire").grid(row=0, column=0)
	Label(frame1, text="Etablissement").grid(row=0,column=2)
	Label(frame1, text="Classe").grid(row=1, column=0)
	Label(frame1, text="Trimestre").grid(row=1, column=2)

	#ListeClasse=["Classe1","Classe2", "Classe3"]
	#ListeEtablissement=["Ecole1","Ecole2", "Ecole3"]
	#ListeNNI_Eleve=["Amina","Mohammed", "Ely"]
	ListeAnneeScolaire=["2020_2021","2021_2022", "2022_2023","2023_2024","2024_2025"]
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
	e4 = ttk.Combobox(frame1,values=ListeTrimestre)

	e1.grid(row=0, column=1)
	e2.grid(row=0, column=3)
	e3.grid(row=1, column=1)
	e4.grid(row=1, column=3)

	e=Entry(frame2)
	e.configure(state=DISABLED)

	#ligne0, 
	e00=Entry(frame2)
	e00.configure(bg='light green')
	e01=Entry(frame2)
	e01.configure(bg='light green')
	e02=Entry(frame2)
	e02.configure(bg='light green')
	e03=Entry(frame2)
	e03.configure(bg='light green')
	e04=Entry(frame2)
	e04.configure(bg='light green')
	e05=Entry(frame2)
	e05.configure(bg='light green')
	e06=Entry(frame2)	
	e06.configure(bg='light green')
	e07=Entry(frame2)
	e07.configure(bg='light green')
	e08=Entry(frame2)
	e08.configure(bg='light green')
	e09=Entry(frame2)
	e09.configure(bg='light green')


	#ligne0, 
	e10=Entry(frame2)
	e10.insert(0,"Lundi")
	e10.configure(bg='orange')
	e11=Entry(frame2)
	e12=Entry(frame2)
	e13=Entry(frame2)
	e14=Entry(frame2)
	e15=Entry(frame2)
	e16=Entry(frame2)
	e17=Entry(frame2)
	e18=Entry(frame2)
	e19=Entry(frame2)
	e120=Entry(frame2)

	#ligne0, 
	e20=Entry(frame2)
	e20.insert(0,"Mardi")
	e20.configure(bg='orange')
	e21=Entry(frame2)
	e22=Entry(frame2)
	e23=Entry(frame2)
	e24=Entry(frame2)
	e25=Entry(frame2)
	e26=Entry(frame2)
	e27=Entry(frame2)
	e28=Entry(frame2)
	e29=Entry(frame2)
	e230=Entry(frame2)

	#ligne0, 
	e30=Entry(frame2)
	e30.insert(0,"Mercredi")
	e30.configure(bg='orange')
	e31=Entry(frame2)
	e32=Entry(frame2)
	e33=Entry(frame2)
	e34=Entry(frame2)
	e35=Entry(frame2)
	e36=Entry(frame2)
	e37=Entry(frame2)
	e38=Entry(frame2)
	e39=Entry(frame2)
	e340=Entry(frame2)

	#ligne0, 
	e40=Entry(frame2)
	e40.insert(0,"Jeudi")
	e40.configure(bg='orange')
	e41=Entry(frame2)
	e42=Entry(frame2)
	e43=Entry(frame2)
	e44=Entry(frame2)
	e45=Entry(frame2)
	e46=Entry(frame2)
	e47=Entry(frame2)
	e48=Entry(frame2)
	e49=Entry(frame2)
	e450=Entry(frame2)

	#ligne0, 
	e50=Entry(frame2)
	e50.insert(0,"Vendredi")
	e50.configure(bg='orange')
	e51=Entry(frame2)
	e52=Entry(frame2)
	e53=Entry(frame2)
	e54=Entry(frame2)
	e55=Entry(frame2)
	e56=Entry(frame2)
	e57=Entry(frame2)
	e58=Entry(frame2)
	e59=Entry(frame2)
	e560=Entry(frame2)

	#ligne0, 
	e60=Entry(frame2)
	e60.insert(0,"Samedi")
	e60.configure(bg='orange')
	e61=Entry(frame2)
	e62=Entry(frame2)
	e63=Entry(frame2)
	e64=Entry(frame2)
	e65=Entry(frame2)
	e66=Entry(frame2)
	e67=Entry(frame2)
	e68=Entry(frame2)
	e69=Entry(frame2)
	e670=Entry(frame2)

	#ligne0, 
	e70=Entry(frame2)
	e70.insert(0,"Dimanche")
	e70.configure(bg='orange')
	e71=Entry(frame2)
	e72=Entry(frame2)
	e73=Entry(frame2)
	e74=Entry(frame2)
	e75=Entry(frame2)
	e76=Entry(frame2)
	e77=Entry(frame2)
	e78=Entry(frame2)
	e79=Entry(frame2)
	e780=Entry(frame2)

	e.grid(row=0, column=0)

	e00.grid(row=0,column=1)
	e01.grid(row=0,column=2)
	e02.grid(row=0,column=3)
	e03.grid(row=0,column=4)
	e04.grid(row=0,column=5)
	e05.grid(row=0,column=6)
	e06.grid(row=0,column=7)
	e07.grid(row=0,column=8)
	e08.grid(row=0,column=9)
	e09.grid(row=0,column=10)

	e10.grid(row=1,column=0)
	e11.grid(row=1,column=1)
	e12.grid(row=1,column=2)
	e13.grid(row=1,column=3)
	e14.grid(row=1,column=4)
	e15.grid(row=1,column=5)
	e16.grid(row=1,column=6)
	e17.grid(row=1,column=7)
	e18.grid(row=1,column=8)
	e19.grid(row=1,column=9)
	e120.grid(row=1,column=10)

	e20.grid(row=2,column=0)
	e21.grid(row=2,column=1)
	e22.grid(row=2,column=2)
	e23.grid(row=2,column=3)
	e24.grid(row=2,column=4)
	e25.grid(row=2,column=5)
	e26.grid(row=2,column=6)
	e27.grid(row=2,column=7)
	e28.grid(row=2,column=8)
	e29.grid(row=2,column=9)
	e230.grid(row=2,column=10)

	e30.grid(row=3,column=0)
	e31.grid(row=3,column=1)
	e32.grid(row=3,column=2)
	e33.grid(row=3,column=3)
	e34.grid(row=3,column=4)
	e35.grid(row=3,column=5)
	e36.grid(row=3,column=6)
	e37.grid(row=3,column=7)
	e38.grid(row=3,column=8)
	e39.grid(row=3,column=9)
	e340.grid(row=3,column=10)

	e40.grid(row=4,column=0)
	e41.grid(row=4,column=1)
	e42.grid(row=4,column=2)
	e43.grid(row=4,column=3)
	e44.grid(row=4,column=4)
	e45.grid(row=4,column=5)
	e46.grid(row=4,column=6)
	e47.grid(row=4,column=7)
	e48.grid(row=4,column=8)
	e49.grid(row=4,column=9)
	e450.grid(row=4,column=10)

	e50.grid(row=5,column=0)
	e51.grid(row=5,column=1)
	e52.grid(row=5,column=2)
	e53.grid(row=5,column=3)
	e54.grid(row=5,column=4)
	e55.grid(row=5,column=5)
	e56.grid(row=5,column=6)
	e57.grid(row=5,column=7)
	e58.grid(row=5,column=8)
	e59.grid(row=5,column=9)
	e560.grid(row=5,column=10)

	e60.grid(row=6,column=0)
	e61.grid(row=6,column=1)
	e62.grid(row=6,column=2)
	e63.grid(row=6,column=3)
	e64.grid(row=6,column=4)
	e65.grid(row=6,column=5)
	e66.grid(row=6,column=6)
	e67.grid(row=6,column=7)
	e68.grid(row=6,column=8)
	e69.grid(row=6,column=9)
	e670.grid(row=6,column=10)

	e70.grid(row=7,column=0)
	e71.grid(row=7,column=1)
	e72.grid(row=7,column=2)
	e73.grid(row=7,column=3)
	e74.grid(row=7,column=4)
	e75.grid(row=7,column=5)
	e76.grid(row=7,column=6)
	e77.grid(row=7,column=7)
	e78.grid(row=7,column=8)
	e79.grid(row=7,column=9)
	e780.grid(row=7,column=10)

	def ecriture():

		file=str(e1.get())+"/"+"Emploi_Temps"+"/"+str(e2.get())+"/"+str(e4.get())+"/"+str(e3.get())+"/"
		try :
			os.makedirs(file)
			#os.path.join(file,"test.csv")
			path=str(e1.get())+"_"+"emploitemps"+"_"+"_"+str(e4.get())+"_"+str(e3.get())+".csv"

			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')
				w.writerow([e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get(),e05.get(),e06.get(),e07.get(),e08.get(),e09.get()])
				w.writerow([e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get(),e120.get()])
				w.writerow([e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get(),e26.get(),e27.get(),e28.get(),e29.get(),e230.get()])
				w.writerow([e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get(),e36.get(),e37.get(),e38.get(),e39.get(),e340.get()])
				w.writerow([e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get(),e46.get(),e47.get(),e48.get(),e49.get(),e450.get()])
				w.writerow([e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get(),e56.get(),e57.get(),e58.get(),e59.get(),e560.get()])
				w.writerow([e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get(),e66.get(),e67.get(),e68.get(),e69.get(),e670.get()])
				w.writerow([e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get(),e76.get(),e77.get(),e78.get(),e79.get(),e780.get()])

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
			col_width = epw/11
			# Text height is the same as current font size
			th = pdf.font_size
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Emploi du temps:",  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = str(e3.get())+str(e4.get()),  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			"""
			pdf.cell(200, 8, txt = str(e.get())+"|"+str(e00.get())+"|"+str(e01.get())+"|"+str(e02.get())+"|"+str(e03.get())+"|"+str(e04.get())+"|"+str(e05.get())+"|"+str(e06.get())+"|"+str(e07.get())+"|"+str(e08.get())+"|"+str(e09.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e10.get())+"|"+str(e11.get())+"|"+str(e12.get())+"|"+str(e13.get())+"|"+str(e14.get())+"|"+str(e15.get())+"|"+str(e16.get())+"|"+str(e17.get())+"|"+str(e18.get())+"|"+str(e19.get())+"|"+str(e120.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e20.get())+"|"+str(e21.get())+"|"+str(e22.get())+"|"+str(e23.get())+"|"+str(e24.get())+"|"+str(e25.get())+"|"+str(e26.get())+"|"+str(e27.get())+"|"+str(e28.get())+"|"+str(e29.get())+"|"+str(e230.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e30.get())+"|"+str(e31.get())+"|"+str(e32.get())+"|"+str(e33.get())+"|"+str(e34.get())+"|"+str(e35.get())+"|"+str(e36.get())+"|"+str(e37.get())+"|"+str(e38.get())+"|"+str(e39.get())+"|"+str(e340.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e40.get())+"|"+str(e41.get())+"|"+str(e42.get())+"|"+str(e43.get())+"|"+str(e44.get())+"|"+str(e45.get())+"|"+str(e46.get())+"|"+str(e47.get())+"|"+str(e48.get())+"|"+str(e49.get())+"|"+str(e450.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e50.get())+"|"+str(e51.get())+"|"+str(e52.get())+"|"+str(e53.get())+"|"+str(e54.get())+"|"+str(e55.get())+"|"+str(e56.get())+"|"+str(e57.get())+"|"+str(e58.get())+"|"+str(e59.get())+"|"+str(e560.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e60.get())+"|"+str(e61.get())+"|"+str(e62.get())+"|"+str(e63.get())+"|"+str(e64.get())+"|"+str(e65.get())+"|"+str(e66.get())+"|"+str(e67.get())+"|"+str(e68.get())+"|"+str(e69.get())+"|"+str(e670.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e70.get())+"|"+str(e71.get())+"|"+str(e72.get())+"|"+str(e73.get())+"|"+str(e74.get())+"|"+str(e75.get())+"|"+str(e76.get())+"|"+str(e77.get())+"|"+str(e78.get())+"|"+str(e79.get())+"|"+str(e780.get()), ln = 2, align = 'l')
			
			"""
			data=[[str(e.get()),str(e00.get()),str(e01.get()),str(e02.get()),str(e03.get()),str(e04.get()),str(e05.get()),str(e06.get()),str(e07.get()),str(e08.get()),str(e09.get())],
			[str(e10.get()),str(e11.get()),str(e12.get()),str(e13.get()),str(e14.get()),str(e15.get()),str(e16.get()),str(e17.get()),str(e18.get()),str(e19.get()),str(e120.get())],
			[str(e20.get()),str(e21.get()),str(e22.get()),str(e23.get()),str(e24.get()),str(e25.get()),str(e26.get()),str(e27.get()),str(e28.get()),str(e29.get()),str(e230.get())],
			[str(e30.get()),str(e31.get()),str(e32.get()),str(e33.get()),str(e34.get()),str(e35.get()),str(e36.get()),str(e37.get()),str(e38.get()),str(e39.get()),str(e340.get())],
			[str(e40.get()),str(e41.get()),str(e42.get()),str(e43.get()),str(e44.get()),str(e45.get()),str(e46.get()),str(e47.get()),str(e48.get()),str(e49.get()),str(e450.get())],
			[str(e50.get()),str(e51.get()),str(e52.get()),str(e53.get()),str(e54.get()),str(e55.get()),str(e56.get()),str(e57.get()),str(e58.get()),str(e59.get()),str(e560.get())],
			[str(e60.get()),str(e61.get()),str(e62.get()),str(e63.get()),str(e64.get()),str(e65.get()),str(e66.get()),str(e67.get()),str(e68.get()),str(e69.get()),str(e670.get())],
			[str(e70.get()),str(e71.get()),str(e72.get()),str(e73.get()),str(e74.get()),str(e75.get()),str(e76.get()),str(e77.get()),str(e78.get()),str(e79.get()),str(e780.get())]]

			for row in data:
			    for datum in row:
			        # Enter data in colums
			        # Notice the use of the function str to coerce any input to the 
			        # string type. This is needed
			        # since pyFPDF expects a string, not a number.
			        pdf.cell(col_width, th, str(datum), border=1)
			 
			    pdf.ln(th)

			  
			# save the pdf with name .pdf 
			fiche_emploi_temps=file+"emploi_temps"+".pdf"
			pdf.output(fiche_emploi_temps)

		except :
			path=str(e1.get())+"_"+"emploitemps"+"_"+"_"+str(e4.get())+"_"+str(e3.get())+".csv"

			with open (file+path,'a', newline='')  as files :
				w=csv.writer(files,delimiter=',',lineterminator='\n')

				w.writerow([e.get(),e00.get(),e01.get(),e02.get(),e03.get(),e04.get(),e05.get(),e06.get(),e07.get(),e08.get(),e09.get()])
				w.writerow([e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get(),e120.get()])
				w.writerow([e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get(),e26.get(),e27.get(),e28.get(),e29.get(),e230.get()])
				w.writerow([e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),e35.get(),e36.get(),e37.get(),e38.get(),e39.get(),e340.get()])
				w.writerow([e40.get(),e41.get(),e42.get(),e43.get(),e44.get(),e45.get(),e46.get(),e47.get(),e48.get(),e49.get(),e450.get()])
				w.writerow([e50.get(),e51.get(),e52.get(),e53.get(),e54.get(),e55.get(),e56.get(),e57.get(),e58.get(),e59.get(),e560.get()])
				w.writerow([e60.get(),e61.get(),e62.get(),e63.get(),e64.get(),e65.get(),e66.get(),e67.get(),e68.get(),e69.get(),e670.get()])
				w.writerow([e70.get(),e71.get(),e72.get(),e73.get(),e74.get(),e75.get(),e76.get(),e77.get(),e78.get(),e79.get(),e780.get()])

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
			col_width = epw/11
			# Text height is the same as current font size
			th = pdf.font_size
			  
			# create a cell 
			

			pdf.cell(200, 10, txt = "Emploi du temps:",  
			         ln = 1, align = 'C') 
			pdf.cell(200, 10, txt = str(e3.get())+" "+str(e4.get()),  
			         ln = 1, align = 'C') 
			  
			# add another cell 
			"""
			pdf.cell(200, 8, txt = str(e.get())+"|"+str(e00.get())+"|"+str(e01.get())+"|"+str(e02.get())+"|"+str(e03.get())+"|"+str(e04.get())+"|"+str(e05.get())+"|"+str(e06.get())+"|"+str(e07.get())+"|"+str(e08.get())+"|"+str(e09.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e10.get())+"|"+str(e11.get())+"|"+str(e12.get())+"|"+str(e13.get())+"|"+str(e14.get())+"|"+str(e15.get())+"|"+str(e16.get())+"|"+str(e17.get())+"|"+str(e18.get())+"|"+str(e19.get())+"|"+str(e120.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e20.get())+"|"+str(e21.get())+"|"+str(e22.get())+"|"+str(e23.get())+"|"+str(e24.get())+"|"+str(e25.get())+"|"+str(e26.get())+"|"+str(e27.get())+"|"+str(e28.get())+"|"+str(e29.get())+"|"+str(e230.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e30.get())+"|"+str(e31.get())+"|"+str(e32.get())+"|"+str(e33.get())+"|"+str(e34.get())+"|"+str(e35.get())+"|"+str(e36.get())+"|"+str(e37.get())+"|"+str(e38.get())+"|"+str(e39.get())+"|"+str(e340.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e40.get())+"|"+str(e41.get())+"|"+str(e42.get())+"|"+str(e43.get())+"|"+str(e44.get())+"|"+str(e45.get())+"|"+str(e46.get())+"|"+str(e47.get())+"|"+str(e48.get())+"|"+str(e49.get())+"|"+str(e450.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e50.get())+"|"+str(e51.get())+"|"+str(e52.get())+"|"+str(e53.get())+"|"+str(e54.get())+"|"+str(e55.get())+"|"+str(e56.get())+"|"+str(e57.get())+"|"+str(e58.get())+"|"+str(e59.get())+"|"+str(e560.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e60.get())+"|"+str(e61.get())+"|"+str(e62.get())+"|"+str(e63.get())+"|"+str(e64.get())+"|"+str(e65.get())+"|"+str(e66.get())+"|"+str(e67.get())+"|"+str(e68.get())+"|"+str(e69.get())+"|"+str(e670.get()), ln = 2, align = 'l') 
			pdf.cell(200, 8, txt = str(e70.get())+"|"+str(e71.get())+"|"+str(e72.get())+"|"+str(e73.get())+"|"+str(e74.get())+"|"+str(e75.get())+"|"+str(e76.get())+"|"+str(e77.get())+"|"+str(e78.get())+"|"+str(e79.get())+"|"+str(e780.get()), ln = 2, align = 'l')
			
			"""
			data=[[str(e.get()),str(e00.get()),str(e01.get()),str(e02.get()),str(e03.get()),str(e04.get()),str(e05.get()),str(e06.get()),str(e07.get()),str(e08.get()),str(e09.get())],
			[str(e10.get()),str(e11.get()),str(e12.get()),str(e13.get()),str(e14.get()),str(e15.get()),str(e16.get()),str(e17.get()),str(e18.get()),str(e19.get()),str(e120.get())],
			[str(e20.get()),str(e21.get()),str(e22.get()),str(e23.get()),str(e24.get()),str(e25.get()),str(e26.get()),str(e27.get()),str(e28.get()),str(e29.get()),str(e230.get())],
			[str(e30.get()),str(e31.get()),str(e32.get()),str(e33.get()),str(e34.get()),str(e35.get()),str(e36.get()),str(e37.get()),str(e38.get()),str(e39.get()),str(e340.get())],
			[str(e40.get()),str(e41.get()),str(e42.get()),str(e43.get()),str(e44.get()),str(e45.get()),str(e46.get()),str(e47.get()),str(e48.get()),str(e49.get()),str(e450.get())],
			[str(e50.get()),str(e51.get()),str(e52.get()),str(e53.get()),str(e54.get()),str(e55.get()),str(e56.get()),str(e57.get()),str(e58.get()),str(e59.get()),str(e560.get())],
			[str(e60.get()),str(e61.get()),str(e62.get()),str(e63.get()),str(e64.get()),str(e65.get()),str(e66.get()),str(e67.get()),str(e68.get()),str(e69.get()),str(e670.get())],
			[str(e70.get()),str(e71.get()),str(e72.get()),str(e73.get()),str(e74.get()),str(e75.get()),str(e76.get()),str(e77.get()),str(e78.get()),str(e79.get()),str(e780.get())]]

			for row in data:
			    for datum in row:
			        # Enter data in colums
			        # Notice the use of the function str to coerce any input to the 
			        # string type. This is needed
			        # since pyFPDF expects a string, not a number.
			        pdf.cell(col_width, th, str(datum), border=1)
			 
			    pdf.ln(th)

			  
			# save the pdf with name .pdf 
			fiche_emploi_temps=file+"emploi_temps"+".pdf"
			pdf.output(fiche_emploi_temps)


		mb.showinfo("alerte", "Les informations ont bien été enregistrées")

	def impression():
		# save FPDF() class into a  
		# variable pdf 
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
		col_width = epw/11
		# Text height is the same as current font size
		th = pdf.font_size
		  
		# create a cell 
		

		pdf.cell(200, 10, txt = "Emploi du temps:",  
		         ln = 1, align = 'C') 
		pdf.cell(200, 10, txt = str(e3.get())+" "+str(e4.get()),  
		         ln = 1, align = 'C') 
		  
		# add another cell 
		"""
		pdf.cell(200, 8, txt = str(e.get())+"|"+str(e00.get())+"|"+str(e01.get())+"|"+str(e02.get())+"|"+str(e03.get())+"|"+str(e04.get())+"|"+str(e05.get())+"|"+str(e06.get())+"|"+str(e07.get())+"|"+str(e08.get())+"|"+str(e09.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e10.get())+"|"+str(e11.get())+"|"+str(e12.get())+"|"+str(e13.get())+"|"+str(e14.get())+"|"+str(e15.get())+"|"+str(e16.get())+"|"+str(e17.get())+"|"+str(e18.get())+"|"+str(e19.get())+"|"+str(e120.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e20.get())+"|"+str(e21.get())+"|"+str(e22.get())+"|"+str(e23.get())+"|"+str(e24.get())+"|"+str(e25.get())+"|"+str(e26.get())+"|"+str(e27.get())+"|"+str(e28.get())+"|"+str(e29.get())+"|"+str(e230.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e30.get())+"|"+str(e31.get())+"|"+str(e32.get())+"|"+str(e33.get())+"|"+str(e34.get())+"|"+str(e35.get())+"|"+str(e36.get())+"|"+str(e37.get())+"|"+str(e38.get())+"|"+str(e39.get())+"|"+str(e340.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e40.get())+"|"+str(e41.get())+"|"+str(e42.get())+"|"+str(e43.get())+"|"+str(e44.get())+"|"+str(e45.get())+"|"+str(e46.get())+"|"+str(e47.get())+"|"+str(e48.get())+"|"+str(e49.get())+"|"+str(e450.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e50.get())+"|"+str(e51.get())+"|"+str(e52.get())+"|"+str(e53.get())+"|"+str(e54.get())+"|"+str(e55.get())+"|"+str(e56.get())+"|"+str(e57.get())+"|"+str(e58.get())+"|"+str(e59.get())+"|"+str(e560.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e60.get())+"|"+str(e61.get())+"|"+str(e62.get())+"|"+str(e63.get())+"|"+str(e64.get())+"|"+str(e65.get())+"|"+str(e66.get())+"|"+str(e67.get())+"|"+str(e68.get())+"|"+str(e69.get())+"|"+str(e670.get()), ln = 2, align = 'l') 
		pdf.cell(200, 8, txt = str(e70.get())+"|"+str(e71.get())+"|"+str(e72.get())+"|"+str(e73.get())+"|"+str(e74.get())+"|"+str(e75.get())+"|"+str(e76.get())+"|"+str(e77.get())+"|"+str(e78.get())+"|"+str(e79.get())+"|"+str(e780.get()), ln = 2, align = 'l')
		
		"""
		data=[[str(e.get()),str(e00.get()),str(e01.get()),str(e02.get()),str(e03.get()),str(e04.get()),str(e05.get()),str(e06.get()),str(e07.get()),str(e08.get()),str(e09.get())],
		[str(e10.get()),str(e11.get()),str(e12.get()),str(e13.get()),str(e14.get()),str(e15.get()),str(e16.get()),str(e17.get()),str(e18.get()),str(e19.get()),str(e120.get())],
		[str(e20.get()),str(e21.get()),str(e22.get()),str(e23.get()),str(e24.get()),str(e25.get()),str(e26.get()),str(e27.get()),str(e28.get()),str(e29.get()),str(e230.get())],
		[str(e30.get()),str(e31.get()),str(e32.get()),str(e33.get()),str(e34.get()),str(e35.get()),str(e36.get()),str(e37.get()),str(e38.get()),str(e39.get()),str(e340.get())],
		[str(e40.get()),str(e41.get()),str(e42.get()),str(e43.get()),str(e44.get()),str(e45.get()),str(e46.get()),str(e47.get()),str(e48.get()),str(e49.get()),str(e450.get())],
		[str(e50.get()),str(e51.get()),str(e52.get()),str(e53.get()),str(e54.get()),str(e55.get()),str(e56.get()),str(e57.get()),str(e58.get()),str(e59.get()),str(e560.get())],
		[str(e60.get()),str(e61.get()),str(e62.get()),str(e63.get()),str(e64.get()),str(e65.get()),str(e66.get()),str(e67.get()),str(e68.get()),str(e69.get()),str(e670.get())],
		[str(e70.get()),str(e71.get()),str(e72.get()),str(e73.get()),str(e74.get()),str(e75.get()),str(e76.get()),str(e77.get()),str(e78.get()),str(e79.get()),str(e780.get())]]

		for row in data:
		    for datum in row:
		        # Enter data in colums
		        # Notice the use of the function str to coerce any input to the 
		        # string type. This is needed
		        # since pyFPDF expects a string, not a number.
		        pdf.cell(col_width, th, str(datum), border=1)
		 
		    pdf.ln(th)



		  
		# save the pdf with name .pdf 
		fiche_emploi_temps="emploi_temps"+str(e3.get())+"_"+str(e4.get())+"_"+".pdf"
		pdf.output(fiche_emploi_temps)
		webbrowser.open_new(fiche_emploi_temps)  

	Button(frame3, text ='Imprimer',command=impression).grid(row=0,column=0)
	Button(frame3, text ='Sauver', command=ecriture).grid(row=0,column=1)

