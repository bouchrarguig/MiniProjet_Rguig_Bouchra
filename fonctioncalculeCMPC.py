import sqlite3 as lite
from tkinter import *
from tkinter import ttk
def calculerCMPC():
        

        #la fonction qui calcul le cout moyen pondéré du capital
        def calculeCMPC():
                try:
                        Ke=ke.get()
                        Ke=float(Ke)
                        Kd=float(kd.get())
                        E=float(e.get())
                        D=float(d.get())
                        V=E+D
                        T=float(tis.get())
                        cmpc=(Ke*(E/V))+(Kd*(1-T)*(D/V))
                        cmpc=cmpc*100
                        #affichage du résultat
                        lblrcmpc=Label(fen,text=cmpc)
                        lblrcmpc.place(x=400,y=300)
                        return(cmpc)
                        
                except:
                        msg=" Erreur de calcul, entrer les valeurs!! "
                        lblr=Label(fen,text=msg)
                        lblr.place(x=50,y=350)
                        

        #création de la fenetre de l'application:
        fen=Tk()
        fen.geometry("800x600")
        fen.title("Calcul de CMPC: ")
        fen.minsize(800,600)
        fen.iconbitmap("logo.ico")
        fen.config(background='#FFC0CB')
        lbltitre=Label(fen,text="CALCUL DU COÛT MOYEN PONDÉRÉ DU CAPITAL",font=("Courier",24),bg='#77b5fe',fg='white')
        lbltitre.pack()
        #width=200
        #height=200
        #image=PhotoImage(file="finance2.png").zoom(35).subsample(32)
        #canvas=Canvas(fen, width=width, height=height, bg='#4065A4' ,bd=0, highlightthickness=0)
        #canvas.create_image(width/2,height/2,image=image)
        #canvas.pack()
        #canvas.place(x=550,y=50)
        # les données pour le calcul de CMPC:
        lblke=Label(fen,text="Entrer le taux risqué de la société(Ke):" )
        lblke.place(x=50,y=50)
        ke=Entry(fen)
        ke.place(x=400,y=50)

        lblkd=Label(fen,text="Entrer le taux normatif de la dette(Kd):")
        lblkd.place(x=50,y=100)
        kd=Entry(fen)
        kd.place(x=400,y=100)
        
        lble=Label(fen,text="Entrer la valeur de marché des capitaux propres (E):")
        lble.place(x=50,y=150)
        e=Entry(fen)
        e.place(x=400,y=150)

        lbld=Label(fen,text="Entrer la valeur de la dette nette (D):")
        lbld.place(x=50,y=200)
        d=Entry(fen)
        d.place(x=400,y=200)

        lbltis=Label(fen,text="Entrer le taux de l'impôt sur le société(IS):")
        lbltis.place(x=50,y=250)
        tis=Entry(fen)
        tis.place(x=400,y=250)
   
        
        #bouton pour le calcul:
        calculerCMPC=Button(fen,text= "Calculer le CMPC en %", command=calculeCMPC)
        calculerCMPC.place(x=100,y=300)
        

        #calculerBFR=Button(fen,text= "Passer au calcul du besoin de fonds de roulement(BFR)", command=calculerBFR)
        #calculerBFR.place(x=800,y=500)
        fen.mainloop()
        
