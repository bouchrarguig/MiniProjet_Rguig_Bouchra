import sqlite3 as lite
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image



#---------------------------------------------------------------------  

def projet():
    
    global nomprojet
    nomprojet=str(nom.get())
    import connexionBD
    connexionBD.projet(nomprojet)
    
 
def calculerCMPC():
    import fonctioncalculeCMPC
    fonctioncalculeCMPC.calculerCMPC()
    
    

    

    
#création de la fenetre de l'application:


fen=Tk()
fen.geometry("400x400")
fen.title("Accueil : Etude du rendement de projet")
fen.minsize(800,600)
fen.iconbitmap("logo.ico")
fen.config(background='#FFC0CB')
lbltitre=Label(fen,text="ETUDE DE VOTRE PROJET D'INVESTISSEMENT",font=("Courier",24),bg='#77b5fe',fg='white')
lbltitre.pack()


width=200
height=200
image=PhotoImage(file="finance.gif").zoom(35).subsample(32)
canvas=Canvas(fen, width=width, height=height, bg='#4065A4' ,bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.pack()
canvas.place(x=550,y=150)

lbl1=Label(fen,text="Entrer le nom de votre projet +(.sqlite)" )
lbl1.place(x=50,y=150)
nom=Entry(fen)
nom.place(x=300,y=150)

lbl2=Label(fen,text="Passer à l'interface de CMPC")
lbl2.place(x=50,y=200)

calculer=Button(fen,text= "Calculer le CMPC de projet", command=calculerCMPC)
calculer.place(x=300,y=200)

commancer=Button(fen,text= " Creér et évaluer le rendement de votre projet !!", command=projet)
commancer.place(x=150,y=270)


fen.mainloop()

