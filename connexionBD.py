import sqlite3 as lite
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from math import sqrt 


def projet(nomprojet):
    
    
    connection = None
    try:
        
        # se connecter à une base de données après sa création
        
        connection = lite.connect(nomprojet)
        # récupérer le curseur d'exécution
        cursor = connection.cursor()
        # la chaîne contenant la requête de création de la table depense d'investissement
        req_DI = '''CREATE TABLE IF NOT EXISTS DI (
                    di_en_KDH TEXT NOT NULL,
                    n1 REAL NOT NULL,
                    n2 REAL NOT NULL,
                    n3 REAL NOT NULL,
                    n4 REAL NOT NULL,
                    n5 REAL NOT NULL,
                    n6 REAL NOT NULL,
                    PRIMARY KEY (di_en_KDH));'''
        req_DBFR = '''CREATE TABLE IF NOT EXISTS DBFR (
                    dbfr_en_KDH TEXT NOT NULL,
                    n1 REAL NOT NULL,
                    n2 REAL NOT NULL,
                    n3 REAL NOT NULL,
                    n4 REAL NOT NULL,
                    n5 REAL NOT NULL,
                    n6 REAL NOT NULL,
                    PRIMARY KEY (dbfr_en_KDH));'''
        req_CF = '''CREATE TABLE IF NOT EXISTS CF (
                    cf_en_KDH TEXT NOT NULL,
                    n1 REAL NOT NULL,
                    n2 REAL NOT NULL,
                    n3 REAL NOT NULL,
                    n4 REAL NOT NULL,
                    n5 REAL NOT NULL,
                    n6 REAL NOT NULL,
                    PRIMARY KEY (cf_en_KDH));'''
        # exécuter cette requête de création
        cursor.execute(req_DI)
        cursor.execute(req_DBFR)
        cursor.execute(req_CF)

    #traitement du projet
    #fonction qui affiche le fenetre qui calcul le besoin en fonds de roulement
        
        
          
        def calculerCMPC():
            import fonctioncalculeCMPC
            fonctioncalculeCMPC.calculerCMPC()
            return(cmpc)
        

        def action(event):
            anneedepense=annee.get()# recuperer la valeur de combobox
           
        def calculerCAHT():
            
            import fonctionCAHT
            fonctionCAHT.calculerCAHT(nomprojet)
            

        #la fonction qui ajoute des depense dans la table Depenses d'investissement:
        def ajouterDepennse():
            valdepense=str(depense.get())
            valmontant=(montant.get())
            valannee=annee.get()
            #print(valdepense)
            #print(valmontant)
            #print(annee.get())
            # créer la liste des tuples de la table DI
           #test selon la valeur de l'année enn va choisir la case de la table  
            if valannee=="n1":
                DI =[( valdepense,valmontant ,0 ,0 ,0 ,0 ,0),]
            elif valannee=="n2":
                DI =[( valdepense,0 ,valmontant ,0 ,0 , 0,0),]
            elif valannee=="n3":
                DI =[( valdepense, 0, 0,valmontant, 0, 0,0),]
            elif valannee=="n4":
                DI =[( valdepense,0 , 0, 0,valmontant , 0,0),]
            elif valannee=="n5":
                DI =[( valdepense, 0, 0,0 , 0,valmontant, 0),]
            else:
                DI =[( valdepense, 0,0 ,0 ,0 ,0 ,valmontant),]
              
            # Exécuter la requête d'insertion
            cursor.executemany('''INSERT INTO
                   DI(di_en_KDH, n1 , n2 ,n3,n4,n5,n6 )
                  VALUES(?, ?, ?, ?,?,?,?)''', DI)
            connection.commit()
            
            print("ajout de depense bien passé !!")

        #fonction de la suppression d'un investissement deja ajouté:
        def supprimerDepense():
            valdepense=str(depense.get())
            
            req='''DELETE FROM
                   DI WHERE di_en_KDH = ?'''
            cursor.execute(req,(valdepense, ))
            connection.commit()
            
            print("Suppression de depense bien passé !!")
                
        #la fonction qui affiche les depenses enregistrés pour un projet d'investissement:
        def afficherDepense():
            req='SELECT * FROM DI'
            result=cursor.execute(req)
        # tableau pour l'affichage des données de la table DI:
            lblr1=Label(fen,text="LE DI EN KDH")
            lblr1.place(x=50,y=300)
            lblr2=Label(fen,text="N1")
            lblr2.place(x=200,y=300)
            lblr3=Label(fen,text="N2")
            lblr3.place(x=350,y=300)
            lblr4=Label(fen,text="N3")
            lblr4.place(x=500,y=300)
            lblr5=Label(fen,text="N4")
            lblr5.place(x=650,y=300)
            lblr6=Label(fen,text="N5")
            lblr6.place(x=800,y=300)
            lblr7=Label(fen,text="N6")
            lblr7.place(x=950,y=300)
            vy=310
            for row in result:
                    #print(row[0])
                    vy=vy+40
                    lbl0=lblr1=Label(fen,text=row[0])
                    lbl0.place(x=50,y=vy)
                    lbl1=lblr1=Label(fen,text=row[1])
                    lbl1.place(x=200,y=vy)
                    lbl2=lblr1=Label(fen,text=row[2])
                    lbl2.place(x=350,y=vy)
                    lbl3=lblr1=Label(fen,text=row[3])
                    lbl3.place(x=500,y=vy)
                    lbl4=lblr1=Label(fen,text=row[4])
                    lbl4.place(x=650,y=vy)
                    lbl5=lblr1=Label(fen,text=row[5])
                    lbl5.place(x=800,y=vy)
                    lbl6=lblr1=Label(fen,text=row[6])
                    lbl6.place(x=950,y=vy)
               # print(req.fetchall())
            return
        #focntion qui calcule le depense d'investissement de tout le projet:
        def calculerDi():
            connection = lite.connect(nomprojet)
            # récupérer le curseur d'exécution
            cursor = connection.cursor()
            c=float(cmpc.get())
            
            value="DI en KDH"
            value2="DI+DBFR"
            value3="DI actualisé"
            t1=0
            t2=0
            t3=0
            t4=0
            t5=0
            t6=0

            tt1=0
            tt2=0
            tt3=0
            tt4=0
            tt5=0
            tt6=0
            
            r='SELECT * FROM DI'
            resultat=cursor.execute(r)
            for row in resultat:
                    t1=row[1]
                    tt1=tt1+t1
                    d1=tt1
                    
                    t2=row[2]
                    tt2=tt2+t2
                    d2=tt2

                    t3=row[3]
                    tt3=tt3+t3
                    d3=tt3

                    t4=row[4]
                    tt4=tt4+t4
                    d4=tt4

                    t5=row[5]
                    tt5=tt5+t5
                    d5=tt5

                    t6=row[6]
                    tt6=tt6+t6
                    d6=tt6
                    
                    
            #print(d1,d2,d3,d4,d5,d6)
            D =[( value,d1,d2,d3,d4,d5,d6),]
              
            # Exécuter la requête d'insertion
            cursor.executemany('''INSERT INTO
                   DI(di_en_KDH, n1 , n2 ,n3,n4,n5,n6 )
                  VALUES(?, ?, ?, ?,?,?,?)''', D)
            connection.commit()
            r2='SELECT * FROM DBFR where dbfr_en_KDH="DELTA/BFR"'

            resul=cursor.execute(r2)
            for row in resul:
                d1=d1+row[1]
                dd1=d1*((1+c)**(0))
                d2=d2+row[2]
                dd2=d2*((1+c)**(-1))
                d3=d3+row[3]
                dd3=d3*((1+c)**(-2))
                d4=d4+row[4]
                dd4=d4*((1+c)**(-3))
                d5=d5+row[5]
                dd5=d5*((1+c)**(-4))
                d6=d6+row[6]
                dd6=d6*((1+c)**(-5))
                
                
                    
            #print(d1,d2,d3,d4,d5,d6)
            #print(dd1,dd2,dd3,dd4,dd5,dd6)
            D2 =[( value2,d1,d2,d3,d4,d5,d6),( value3,dd1,dd2,dd3,dd4,dd5,dd6)]
            cursor.executemany('''INSERT INTO
                   DI(di_en_KDH, n1 , n2 ,n3,n4,n5,n6 )
                  VALUES(?, ?, ?, ?,?,?,?)''', D2)
            connection.commit()
      
        #création de la fenetre de l'application:
        fen=Tk()
        fen.geometry("1080x1000")
        fen.title("Calcul des dépenses d'investissement : ")
        fen.minsize(800,600)
        fen.iconbitmap("logo.ico")
        fen.config(background='#FFC0CB')
        lbltitre=Label(fen,text="CALCUL DE DEPENSE D'INVESTISSEMENT DU PROJET",font=("Courier",24),bg='#77b5fe',fg='white')
        lbltitre.pack()
        
        

        lbl1=Label(fen,text="Entrer le nom du dépense d'investissement" )
        lbl1.place(x=50,y=50)
        depense=Entry(fen)
        depense.place(x=300,y=50)

        # les données de la table dépense d'investissement:

        lbl2=Label(fen,text="Entrer le montant de ce dépense")
        lbl2.place(x=50,y=100)
        montant=Entry(fen)
        montant.place(x=300,y=100)



        lbl3=Label(fen,text="Choisir l'année de ce dépense")
        lbl3.place(x=50,y=150)
        listeAnnee=["n1","n2","n3","n4","n5","n6"]
        annee=ttk.Combobox(fen,values=listeAnnee)
        annee.current(0)
        annee.pack()
        annee.place(x=300,y=150)
        # associe une action au combobox
        annee.bind("<<ComboboxSelected>>",action)
        #bouton pour l'ajout des dépenses
        ajouter=Button(fen,text= "Ajouter le dépense", command=ajouterDepennse)
        ajouter.place(x=100,y=200)
        #bouton pour l'affichage des dépenses:

        afficher=Button(fen,text= "Afficher les dépenses de ce projet",
                        command=afficherDepense)
        afficher.place(x=250,y=200)

        #bouton pour supprimer un depense d'investissemennt:
        supprimer=Button(fen,text= "Supprimer un depense d'investissement",
                        command=supprimerDepense)
        supprimer.place(x=100,y=250)


        #bouton pour le calcule de dépense d'investissement global:

        lblcmpc=Label(fen,text="Entrer le cmpc calculé" )
        lblcmpc.place(x=500,y=250)
        cmpc=Entry(fen)
        cmpc.place(x=700,y=250)

        calculer=Button(fen,text= "Calculer le DI du projet", command=calculerDi)
        calculer.place(x=350,y=250)

        calculerBfr=Button(fen,text= "Passer au calcul du besoin de fonds de roulement(BFR)", command=calculerCAHT)
        calculerBfr.place(x=300,y=660)
        fen.mainloop()
       
       
        if connection != None:
             connection.close()
             connection = None
    except lite.Error as e:
        print("Erreur de connexion à la base de données : ", e.args[0])
        if connection != None:
            connection.close()


    #---------------------------------------------------------------------  






  
