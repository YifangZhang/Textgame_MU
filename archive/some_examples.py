# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import tkinter

## init the Tk screen
top = Tk()
top.geometry("600x800")

## button section ##
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)

## drawing canvas ##
C = Canvas(top, bg = "blue", height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()

## checkbox section ##
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack(side = LEFT)
C2.pack(side = LEFT)

## entry section ##
L1 = Label(top, text = "User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = LEFT)

## tkinter frame ##
'''
frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Red", fg = "red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)
'''

## label section ##
var = StringVar()
label = Label( top, textvariable = var, relief = RAISED )
var.set("Hey!? How are you doing?")
label.pack(side = LEFT)

## list example ##
Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

## menu button example ## still has problem
'''
mb =  Menubutton ( top, text = "condiments", relief = RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label = "mayo",
                          variable = mayoVar )
mb.menu.add_checkbutton ( label = "ketchup",
                          variable = ketchVar )

mb.pack()
'''

## mainloop ##
top.mainloop()
