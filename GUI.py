from tkinter import *
from tkinter.filedialog import askopenfile
import os 
from PIL import ImageTk,Image
from Backed import * 


class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.config(bg="black")
		self.geometry("1038x1910")		
		self.title("Alvin's PhotoShop")
		self.sc_height=self.winfo_screenheight()
		self.sc_width=self.winfo_screenwidth()
	 			
	def CanvasWindow(self):
		self.canvas=Canvas(self,width=1040,height=1700,bg="grey")	
		self.canvas.pack(fill='x',padx=20,pady=20)
		
	def EditingBar(self):
		#=========creating Editing menu=========#
		self.EditingMenu=Menu(self)
		self.EditingMenu.add_command(label="Open",command=self.HackImage)
		self.EditingMenu.add_command(label="Crop",command=lambda:self.OpenScale("Crop"))
		self.EditingMenu.add_command(label="Contrast",command=lambda:self.OpenScale("Contrast"))
		self.EditingMenu.add_command(label="Brightness",command=lambda:self.OpenScale("Brightness"))
		self.EditingMenu.add_command(label="Sharpness",command=lambda:self.OpenScale("Sharpness"))
		self.EditingMenu.add_command(label="Blur",command=lambda:self.OpenScale("Blur"))
		self.EditingMenu.add_command(label="Clear")					
		#=========configing Menu===========#
		self.config(menu=self.EditingMenu)	
		
	def OpenScale(self,name):
		try:
			self.scale.destroy()
		except:
			None
		self.scale=Scale(self,from_=-10,to=10,orient=HORIZONTAL)
		self.scale.pack(anchor="n",ipadx=840,side="top")
		#self.scale.bind("<Motion>",lambda event:
	
	#Functions 
	def HackImage(self):	
		self.image=askopenfile(mode='r', filetypes=[('Select an Image', '.jpg  .png .jpeg')])
		self.pic=Image.open(self.image.name)
		self.pic=self.pic.resize((self.sc_width-200 ,self.sc_height-400),Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.pic)
		self.canvas.create_image((self.sc_width-80)/2,(self.sc_height-380)/2,image=self.img)
		

if __name__=="__main__":
	app=GUI()
		
	#runnings methods
	app.EditingBar()
	app.CanvasWindow()
	
	#running mainloop
	app.mainloop()
