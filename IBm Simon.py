from tkinter import *

def file_BAS():
	con = Tk()
	con.title("console.%")
	con.geometry('300x102+100+100')
	label = Label(con, text='console/>10 PRINT "hello!" ')
	label.grid(column=0, row=0)
	cons = Label(con, text="hello!")
	cons.grid(column=0, row=1)
def clik():
	tka = Tk()
	tka.title("filemgenanger")
	button = Button(tka, text='"file.BAS"', command=file_BAS)
	button.grid(column=2, row=2)
	tka.geometry('300x102+100+100')
	tka.mainloop()

tk = Tk()
tk.title("GRiD")
tk.geometry('400x250')
filemenonger = Button(tk, text="filemen.", command=clik)
filemenonger.grid(column=0, row=1) 
grid = Label(tk, text="*GRiD offichal")
grid.grid(column=1, row=1)
tk.mainloop()