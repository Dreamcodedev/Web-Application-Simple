from tkinter import *
#import tkinter as Tk
import tkinter.messagebox as mb
import sourcedefender

class LoginFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		
		
		self.label_username=Label(self, text="Username")
		self.label_password=Label(self, text="Password")

		self.entry_username=Entry(self)
		self.entry_password=Entry(self,show="*")

		self.label_username.grid(row=0, sticky=E)
		self.label_password.grid(row=1, sticky=E)
		self.entry_username.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)

		self.checkbox= Checkbutton(self, text="Keep me logged in")
		self.checkbox.grid(columnspan=2)
		
		self.logbtn=Button(self, text="Login", command=self._login_btn_clicked,bg='light blue')
		self.logbtn.grid(columnspan=2)

		
		
		self.logoutbtn=Button(self, text="Logout", command=self.quit,bg='blue')
		self.logoutbtn.grid(columnspan=2)

		self.pack()

	def _login_btn_clicked(self):
		username=self.entry_username.get()
		password=self.entry_password.get()

		if username=="admin" and password=="admin":
			import eschool
		else :
			mb.showerror("Login error", "Incorrect username")

root =Tk()
root.title("connexion")
root.geometry("500x500")
root.configure(bg="light blue")
Lf=LoginFrame(root)
root.iconphoto(True, PhotoImage(file=r"C:\Users\Demba\Desktop\projet_jend\logo1.png"))
#root.call('wm', 'iconphoto', root._w,PhotoImage(file='/home/demba/Documents/projet_jend/logo1.png'))  # Icone du bouton de la fenêtre
#root.iconbimbap('/home/demba/Documents/projet_jend/logo1.png')
#root.after(1000)
root.mainloop()
