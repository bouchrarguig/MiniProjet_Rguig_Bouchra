import sqlite3 as lite
from tkinter import *
from tkinter import ttk

def calculerCAHT(nomprojet):
        # se connecter à une base de données après sa création
        connection = lite.connect(nomprojet)
        # récupérer le curseur d'exécution
        cursor = connection.cursor()
        def action(event):
                # recuperer la valeur de combobox année:
                mode=str(Mode.get())
                if (mode=="La part de marché d'un produit"):
                        
                        lblp1=Label(fen,text="Entrer la part de marché vendues en N1" )
                        lblp1.place(x=50,y=150)
                        p1=Entry(fen)
                        p1.place(x=300,y=150)

                        lblp2=Label(fen,text="Entrer la part de marché vendues en N2" )
                        lblp2.place(x=50,y=180)
                        p2=Entry(fen)
                        p2.place(x=300,y=180)

                        lblp3=Label(fen,text="Entrer la part de marché vendues en N3" )
                        lblp3.place(x=50,y=210)
                        p3=Entry(fen)
                        p3.place(x=300,y=210)

                        lblp4=Label(fen,text="Entrer la part de marché vendues en N4" )
                        lblp4.place(x=50,y=240)
                        p4=Entry(fen)
                        p4.place(x=300,y=240)

                        lblp5=Label(fen,text="Entrer la part de marché vendues en N5" )
                        lblp5.place(x=50,y=270)
                        p5=Entry(fen)
                        p5.place(x=300,y=270)

                        lblp6=Label(fen,text="Entrer la part de marché vendues en N6" )
                        lblp6.place(x=50,y=300)
                        p6=Entry(fen)
                        p6.place(x=300,y=300)

                        lbl7=Label(fen,text="Entrer le nombre de jours de BFR" )
                        lbl7.place(x=50,y=360)
                        j=Entry(fen)
                        j.place(x=300,y=360)
                       
                elif (mode=="Quantités vendues * Prix unitaire HT"):
                        lblq1=Label(fen,text="Entrer les quantités vendues en N1" )
                        lblq1.place(x=50,y=150)
                        q1=Entry(fen)
                        q1.place(x=300,y=150)

                        lblq2=Label(fen,text="Entrer les quantités vendues en N2" )
                        lblq2.place(x=50,y=180)
                        q2=Entry(fen)
                        q2.place(x=300,y=180)

                        lblq3=Label(fen,text="Entrer les quantités vendues en N3" )
                        lblq3.place(x=50,y=210)
                        q3=Entry(fen)
                        q3.place(x=300,y=210)

                        lblq4=Label(fen,text="Entrer les quantités vendues en N4" )
                        lblq4.place(x=50,y=240)
                        q4=Entry(fen)
                        q4.place(x=300,y=240)

                        lblq5=Label(fen,text="Entrer les quantités vendues en N5" )
                        lblq5.place(x=50,y=270)
                        q5=Entry(fen)
                        q5.place(x=300,y=270)

                        lblq6=Label(fen,text="Entrer les quantités vendues en N6" )
                        lblq6.place(x=50,y=300)
                        q6=Entry(fen)
                        q6.place(x=300,y=300)
                    
                        lblpru=Label(fen,text="Entrer le Prix unitaire HT en KDH")
                        lblpru.place(x=50,y=330)
                        pru=Entry(fen)
                        pru.place(x=300,y=330)

                        lbl7=Label(fen,text="Entrer le nombre de jours de BFR" )
                        lbl7.place(x=50,y=360)
                        j=Entry(fen)
                        j.place(x=300,y=360)
                   
                        
                                
                                
                def ajout():
                        mode=str(Mode.get())
                        val="CAHT"
                        val1="Prix Unitaire"
                        val2="quantité"
                        val4="BFR"
                        val5="DELTA/BFR"
                        jour=float(j.get())
                        print(jour)
                        jbfr=jour/360
                        print(jbfr)
                        if mode=="La part de marché d'un produit":       
                                
                                caht1=float(p1.get())
                                bfr1=caht1*jbfr
                                dbfr1=bfr1
                                caht2=float(p2.get())
                                bfr2=caht2*jbfr
                                dbfr2=bfr2-bfr1
                                caht3=float(p3.get())
                                bfr3=caht3*jbfr
                                dbfr3=bfr3-bfr2
                                caht4=float(p4.get())
                                bfr4=caht4*jbfr
                                dbfr4=bfr4-bfr3
                                caht5=float(p5.get())
                                bfr5=caht5*jbfr
                                dbfr5=bfr5-bfr4
                                caht6=float(p6.get())
                                bfr6=caht6*jbfr
                                dbfr6=bfr6-bfr5
                                C =[( val, caht1,caht2 ,caht3 ,caht4 ,caht5 ,caht6),( val4, bfr1,bfr2 ,bfr3 ,bfr4 ,bfr5 ,bfr6),( val5, dbfr1,dbfr2 ,dbfr3 ,dbfr4 ,dbfr5 ,dbfr6)]
                        else:    
                                
                                try:
                                        prix=float(pru.get())
                                        print(prix)
                                except:
                                        prix=''
                                quantité1=float(q1.get())
                                caht1=prix*quantité1
                                bfr1=caht1*jbfr
                                dbfr1=bfr1
                        
                                
                                quantité2=float(q2.get())
                                caht2=prix*quantité2
                                bfr2=caht2*jbfr
                                dbfr2=bfr2-bfr1
                       
                                
                                quantité3=float(q3.get())
                                caht3=prix*quantité3
                                bfr3=caht3*jbfr
                                dbfr3=bfr3-bfr2
                       
                                
                                quantité4=float(q4.get())
                                caht4=prix*quantité4
                                bfr4=caht4*jbfr
                                dbfr4=bfr4-bfr3
                        
                                
                                quantité5=float(q5.get())
                                caht5=prix*quantité5
                                bfr5=caht5*jbfr
                                dbfr5=bfr5-bfr4
                        
                                
                                quantité6=float(q6.get())
                                caht6=prix*quantité6
                                bfr6=caht6*jbfr
                                dbfr6=bfr6-bfr5
                
                                C =[( val1, prix,prix ,prix ,prix ,prix ,prix),( val2, quantité1,quantité2 ,quantité3 ,quantité4 ,quantité5 ,quantité6),( val, caht1,caht2 ,caht3 ,caht4 ,caht5 ,caht6),( val4, bfr1,bfr2 ,bfr3 ,bfr4 ,bfr5 ,bfr6),( val5, dbfr1,dbfr2 ,dbfr3 ,dbfr4 ,dbfr5 ,dbfr6)]
                
                        # Exécuter la requête d'insertion
                        cursor.executemany('''INSERT INTO
                        DBFR(dbfr_en_KDH, n1 , n2 ,n3,n4,n5,n6 )
                        VALUES(?, ?, ?, ?,?,?,?)''', C)
                        connection.commit()
                        print("Calcul de CAHT est bien passé !!")
                #bouton ajout 
                ajouter=Button(fen,text= "Ajouter les valeurs a la table CAHT ",command=ajout)
                ajouter.place(x=50,y=400)
                
       
            #fonction de la suppression d'un CAHT deja ajouté:
        def supprimerCAHT():
                val="CAHT"
                val1="Prix Unitaire"
                val2="quantité"
                val4="BFR"
                val5="DELTA/BFR"
                req='''DELETE FROM
                   DBFR WHERE dbfr_en_KDH = ?'''
                cursor.execute(req,(val, ))
                connection.commit()
                req1='''DELETE FROM
                   DBFR WHERE dbfr_en_KDH = ?'''
                cursor.execute(req1,(val1, ))
                connection.commit()
                req2='''DELETE FROM
                   DBFR WHERE dbfr_en_KDH = ?'''
                cursor.execute(req2,(val2, ))
                connection.commit()
                req3='''DELETE FROM
                   DBFR WHERE dbfr_en_KDH = ?'''
                cursor.execute(req3,(val4, ))
                connection.commit()
                req4='''DELETE FROM
                   DBFR WHERE dbfr_en_KDH = ?'''
                cursor.execute(req4,(val5, ))
                connection.commit()
                
                print("Suppression de CAHT est bien passé !!")
                
        #la fonction qui affiche les depenses enregistrés pour un projet d'investissement:
        def afficherCAHT():
                req='SELECT * FROM DBFR'
                result=cursor.execute(req)
                # tableau pour l'affichage des données de la table DI:
                lblr1=Label(fen,text="LE DBFR EN KDH")
                lblr1.place(x=150,y=500)
                lblr2=Label(fen,text="N1")
                lblr2.place(x=300,y=500)
                lblr3=Label(fen,text="N2")
                lblr3.place(x=450,y=500)
                lblr4=Label(fen,text="N3")
                lblr4.place(x=600,y=500)
                lblr5=Label(fen,text="N4")
                lblr5.place(x=750,y=500)
                lblr6=Label(fen,text="N5")
                lblr6.place(x=900,y=500)
                lblr7=Label(fen,text="N6")
                lblr7.place(x=1050,y=500)
                vy=500
                for row in result:
                        #print(row[0])
                        vy=vy+30
                        lbl0=lblr1=Label(fen,text=row[0])
                        lbl0.place(x=150,y=vy)
                        lbl1=lblr1=Label(fen,text=row[1])
                        lbl1.place(x=300,y=vy)
                        lbl2=lblr1=Label(fen,text=row[2])
                        lbl2.place(x=450,y=vy)
                        lbl3=lblr1=Label(fen,text=row[3])
                        lbl3.place(x=600,y=vy)
                        lbl4=lblr1=Label(fen,text=row[4])
                        lbl4.place(x=750,y=vy)
                        lbl5=lblr1=Label(fen,text=row[5])
                        lbl5.place(x=900,y=vy)
                        lbl6=lblr1=Label(fen,text=row[6])
                        lbl6.place(x=1050,y=vy)
                        # print(req.fetchall())

                         
                    
        #-----------------------------------------------------------------------------------------
        def calculer():
                return
          
        #la fonction qui ajoute des données de calcul:
        
        #focntion qui calcule de tout le projet:
        def resultatprojet():
                import fonctioncalculeCF
                fonctioncalculeCF.resultatp(nomprojet)
            

        #création de la fenetre:
        fen=Tk()
        fen.geometry("1200x1000")
        fen.title("Calcul de CAHT et BFR : ")
        fen.minsize(800,600)
        fen.iconbitmap("logo.ico")
        fen.config(background='#FFC0CB')
        lbltitre=Label(fen,text="CALCUL DE CHIFFRE D'AFFAIRE HORS TAXE",font=("Courier",24),bg='#77b5fe',fg='white')
        lbltitre.pack()
        #width=200
        #height=200
        #image=PhotoImage(file="finance1.png").zoom(35).subsample(32)
        #canvas=Canvas(fen, width=width, height=height, bg='#4065A4' ,bd=0, highlightthickness=0)
        #canvas.create_image(width/2,height/2,image=image)
        #canvas.pack()
        #canvas.place(x=550,y=50)
        #recuperation des données:

        lblch1=Label(fen,text="Choisir le mode du calcul de CAHT : ")
        lblch1.place(x=50,y=100)
        Mode=["La part de marché d'un produit","Quantités vendues * Prix unitaire HT"]
        Mode=ttk.Combobox(fen,width =35,values=Mode)
        Mode.current(0)
        Mode.pack()
        Mode.place(x=300,y=100)
        # associe une action au combobox
        Mode.bind("<<ComboboxSelected>>",action)
        
                
        #bouton pour l'affichage des CAHT:

        afficher=Button(fen,text= "Afficher les CAHT en KDH",command=afficherCAHT)
        afficher.place(x=300,y=400)

        #bouton pour supprimer un depense d'investissemennt:
        supprimer=Button(fen,text= "Supprimer un CAHT",command=supprimerCAHT)
        supprimer.place(x=50,y=450)

        #------------------------------------------------------------------
        
        #bouton pour le calcule de CAHT en KDH:

        calculer=Button(fen,text= "Calculer le CAHT du projet", command=calculer)
        calculer.place(x=50,y=850)

        resultatpro=Button(fen,text= "Passer au calcul de cash flow du projet", command=resultatprojet)
        resultatpro.place( x=50,y=450)
        fen.mainloop()
        
