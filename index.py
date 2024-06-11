#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import subprocess, os, sys, runpy
from tkinter import *
 
fenetre = Tk()
 
def alert():
    showinfo("alerte", "Bravo!")
 
 
 
menubar = Menu(fenetre)
 
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New", command=alert)
menu1.add_command(label="Edit", command=alert)
menu1.add_separator()
menu1.add_command(label="Quit", command=quit)
menubar.add_cascade(label="File", menu=menu1)
 
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Cut", command=alert)
menu2.add_command(label="Copy", command=alert)
menu2.add_command(label="Paste", command=alert)
menubar.add_cascade(label="Edit", menu=menu2)
 
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)
 
fenetre.config(menu=menubar)
 
#Frame
 
 
fenetre.mainloop()