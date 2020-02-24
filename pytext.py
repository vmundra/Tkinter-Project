## Tkinter is part of python library so we don't need to install it
import tkinter as tk



class Menubar:

	def __init__(self, parent):

		font_specs = ("windows",9)

		menubar = tk.Menu(parent.master, font = font_specs)

		## thus now in this code, we are creating a menubar and displaying it in the master window
		parent.master.config(menu=menubar)

		## place the dropdown in the menubar
		file_dropdown = tk.Menu(menubar, font = font_specs, tearoff=0) ## this tearoff is passed bcoz else we are able to take the 
		## File menu icon and move it anywhere, thus to keep it stable we pass this argument

		file_dropdown.add_command(label="New File", command=parent.new_file)
		file_dropdown.add_command(label="Open File", command=parent.open_file)
		file_dropdown.add_command(label="Save", command=parent.save)
		file_dropdown.add_command(label="Save As", command=parent.save_as)
		file_dropdown.add_separator()
		file_dropdown.add_command(label="Exit")

		menubar.add_cascade(label = "File" ,menu=file_dropdown, command = parent.master.destroy)


## This is going to be the main class
## functions like open the editor, save n all are going to come over here
class Pytext:

	def __init__(self,master):

		master.title("Vian")
		master.geometry("970x500")

		font_specs = ("windows",11)

		## as master is one of our main window so we need it's access everwhere
		## thus to pass it even in the Menubar class we write this
		self.master = master 

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


		self.menubar = Menubar(self)


	def set_window_title(self):
		pass

	def new_file(self):
		pass

	def open_file(self):
		pass

	def save(self):
		pass

	def save_as(self):
		pass


##this is the code which is going to launch our program
if __name__ == "__main__":

	## master is actually the main window
	master = tk.Tk()
	pt = Pytext(master)
	master.mainloop()





















































