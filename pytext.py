## Tkinter is part of python library so we don't need to install it
import tkinter as tk


## This is going to be the main class
## functions like open the editor, save n all are going to come over here
class Pytext:

	def __init__(self,master):

		master.title("Vian")
		master.geometry("970x500")

		font_specs = ("windows",11)

		self.textarea = tk.Text(master, font = font_specs)
		self.scroll = tk.Scrollbar(master, command = self.textarea.yview) ## yview means that scroll it in the Y-axis direction

		## but we just don't only want to scroll using the side scroll bar
		## that is we don't want to keep clicking the side bar for scrolling
		## but we also want to scroll it using the mouse
		self.textarea.configure(yscrollcommand = self.scroll.set)

		## this line of code is to place the textarea in the left place of scrollbar using geometry commands
		self.textarea.pack(side=tk.LEFT, fill=tk.BOTH , expand=True)
		## so here we say that place it to the left,
		## make it occupy the entire window screen,
		## if u try the third argument to be False, then it won't fit the entire screen, it will just be a square not touching the scrollbar



		## this line of code is to place the scrollbar in the rightmost place using geometry commands
		self.scroll.pack(side=tk.RIGHT, fill = tk.Y)
		## as for the scrollbar we just need it to take the Y-axis space so we write tk.Y


##this is the code which is going to launch our program
if __name__ == "__main__":

	## master is actually the main window
	master = tk.Tk()
	pt = Pytext(master)
	master.mainloop()





















































