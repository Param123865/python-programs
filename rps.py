from tkinter import *
class Mybutton:
	#constructor
	def __init__ (self, root):
		self.c = Canvas(root, bg="white", height=700, width=200)
		#create a frame as child to root window
		self.f = Frame(root, height=400, width=500)
		#let the frame will not shrink
		self.f.propagate(0)
		#attach the fram to root window
		self.f.pack()
		#create 3 push buttons and bind them
		#to buttonClick method and pass a number
		self.b1 = Button(self.f, text='Rock', width=15, height=2, command= lambda: self.buttonClick(1))
		self.b2 = Button(self.f, text='Paper', width=15, height=2, command= lambda: self.buttonClick(2))
		self.b3 = Button(self.f, text='Scissor', width=15, height=2, command= lambda: self.buttonClick(3))
		#attach buttons to the frame
		self.b1.pack()
		self.b2.pack()
		self.b3.pack()
		#method to be called when the button is clicked
		def buttonClick(self, num):
			if num == 1:
				print("You won the match")
			if num == 2:
				print("You clicked Paper but you lost")
			if num == 3:
				print("You won the match")
				#create root window
				root = Tk()
				#create an object to button class
				b = Button(root)
				#the root window  handles the mouse click event
				root.mainloop()