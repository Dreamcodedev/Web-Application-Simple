from tkinter import *
from email.message import EmailMessage
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import webbrowser
from tkinter import messagebox as mb
import os
import csv
from fpdf import FPDF 
import webbrowser
from tkinter import ttk
import sys



#window.iconbitmap

def Message(root): 
	frame1 =LabelFrame(root, borderwidth=3)
	frame1.grid(row=0, column=1, padx=10, pady=10) 

	frame2 =LabelFrame(root, borderwidth=3)
	frame2.grid(row=1, column=1, padx=10, pady=10)

	frame3 =LabelFrame(root, borderwidth=0)
	frame3.grid(row=2, column=1,padx=10, pady=10)

	LabelUser=Label(frame1, text='Votre adresse mail').grid(row=0)
	LabelPassword = Label(frame1, text='Mot de passe').grid(row=1)
	LabelSendUser = Label(frame1, text='Adresse destinataire').grid(row=2)

	e1=Entry(frame1)   # mail du l'expediteur
	e2=Entry(frame1,show="*") # MP de m'expediteur
	e3=Entry(frame1)   # Mail du destinataire

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	#--------------------
	textbox2=Text(frame2,width=50,height=10,bg='light green')
	label2=Label(frame2,text='Message')
	textbox1=Text(frame2,width=50,height=1,bg='light green')
	label1=Label(frame2,text='Sujet')
	textbox3=Text(frame2,width=50,height=1,bg='light green')
	label4=Label(frame2,text='Pièce jointe')

	label3=Label(frame2,text='')
	"""
	def email_alert(subject, body, to):
		msg=EmailMessage()
		msg.set_content(body)
		msg['subject']=subject
		msg['to']=to

		user=e1.get()
		msg['from']=user
		password =e2.get()

		server=smtplib.SMTP("smpt.gmail.com", 587)
		server.starttls()
		server.login(user,password)
		server.send_message(msg)

		server.quit()
	"""

	#if __name__== '__main__':
	def Send() :
		gd= textbox3.get('1.0', 'end-1c')
		dialog=textbox2.get('1.0', 'end-1c')
		subject=textbox1.get('1.0','end-1c')
		body=dialog
		
		try :
			msg = MIMEMultipart()
			msg['From'] = e1.get()
			msg['To'] = e3.get()
			msg['Subject']=textbox1.get('1.0','end-1c')
			body = textbox2.get('1.0','end-1c')




			filename = "Homework Attachment"
			attachment = open(gd, "rb")
			p=MIMEBase('application', 'octet-stream')
			p.set_payload((attachment).read())
			encoders.encode_base64(p)
			p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
			msg.attach(p)
			msg.attach(MIMEText(body, 'plain'))

			#mailserver=smtplib.SMTP("smpt.gmail.com", 587)
			mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			#mailserver.starttls()
			#mailserver.ehlo()
			#mailserver.starttls()
			#mailserver.ehlo()

			mailserver.login(e1.get(), e2.get())
			text=msg.as_string()
			mailserver.sendmail(e1.get(), e3.get(), text)

			mailserver.quit()

			mb.showinfo("alerte", "Votre message a bien été envoyé")
		
		except:
			#email_alert(subject, dialog, "demba.dioop@gmail.com")
			#email_alert(subject, dialog)
			print ('test')

		

		
		
			
		
	def Reset(): 
		textbox1.delete('1.0','end-1c')
		textbox2.delete('1.0','end-1c')
		textbox3.delete('1.0','end-1c')

	def whatsapp():
        
		webbrowser.open_new_tab('https://web.whatsapp.com/')
        



	label1.pack()
	textbox1.pack()
	label4.pack()
	textbox3.pack()
	label2.pack()
	textbox2.pack()
	label3.pack()
	"""
	button1=Button(window, text='Send Email',width=15, height=1, command=Send)
	button1.pack()
	button2=Button(window, text='Reset',width=15, height=1, command=Reset)
	button2.pack(pady=0)
	"""
	button1=Button(frame2,text='Send Email',width=15,height=1, command=Send)
	button1.pack(side='left', anchor='e', expand=True)

	button2=Button(frame2,text='Reset',width=15,height=1, command=Reset)
	button2.pack(side='right', anchor='w', expand=True)

	button3=Button(frame3,text='Whatsapp',width=15,height=1, command=whatsapp)
	button3.configure(bg="green")
	button3.pack(side='bottom', anchor='w', expand=True)


