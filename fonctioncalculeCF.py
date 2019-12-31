import sqlite3 as lite
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from math import sqrt
from decimal import *
def resultatp(nomprojet):
        # se connecter à une base de données après sa création
        connection = lite.connect(nomprojet)
        # récupérer le curseur d'exécution
        cursor = connection.cursor()




               
        def calculerCF():
        #decalaration des variables de calcul:
                
                t1=0
                t2=0
                t3=0
                t4=0
                t5=0
                t6=0
                val="CAHT"
                C1="Charges variables"
                C2="Charges fixes"
                
                value="CF en KDH" # CF en KDH = Résultat net +  Dotations d'amortissement
                value2="Cash_flow+VR" # Cash_flow de la 5 année = Cash_flow 5 + VR
                value3="CF actualisé" # CF actualisé= Cash_flow net  * (1+cmpc)**(-année-1)
                value4="Résultat d'éxploitation" # Résultat d'éxploitation = CAHT- Charges variable - Charges fixes - Dotations d'amortissement
                value5="Résultat net" #   Résultat net= Résultat d'éxploitation - I/Résultat d'éxploitation
                value6="Dotations d'amortissement" # calculé par l'utilisateur
                value7="I/Résultat d'éxploitation" #I/Résultat d'éxploitation = Résultat d'éxploitation * IS(IS=30%)
                try:
                        # ajout des charges variables et fixes de moon projet
                        DT=float(dotation.get())
                        VR=float(Vr.get()) # calculé par l'utilisateur
                        Cfixe=float(cfixe.get())
                        Cv1 =float(cv1.get())
                        Cv2 =float(cv2.get())
                        Cv3 =float(cv3.get())
                        Cv4 =float(cv4.get())
                        Cv5 =float(cv5.get())
                        Cv6=float(cv6.get())
                        c=float(Cmpc.get()) # Récuperer la valeur de CMPC déja calculé au début de l'étude de ton projet 
                except:
                        lbl1m=Label(fen,text="Entrer les valeur pour calculer:")
                        lbl1m.place(x=50,y=100)

                #------------------------------------------------------------------------------

                r='SELECT * FROM DBFR WHERE dbfr_en_KDH="CAHT" '
                res=cursor.execute(r)
                for row in res:
                        
                        t1=row[1]
                        R1=t1-Cv1-Cfixe-DT
                        IS1=R1*0.3
                        RN1=R1-IS1
                        cf1=RN1+DT
                        CFA1=cf1*((1+c)**(-1))
                        
                        t2=row[2]
                        R2=t2-Cv2-Cfixe-DT
                        IS2=R2*0.3
                        RN2=R2-IS2
                        cf2=RN2+DT
                        CFA2=cf2*((1+c)**(-2))
                        
                        t3=row[3]
                        R3=t3-Cv3-Cfixe-DT
                        IS3=R3*0.3
                        RN3=R3-IS3
                        cf3=RN3+DT
                        CFA3=cf3*((1+c)**(-3))
                        
                        t4=row[4]
                        R4=t4-Cv4-Cfixe-DT
                        IS4=R4*0.3
                        RN4=R4-IS4
                        cf4=RN4+DT
                        CFA4=cf4*((1+c)**(-4))
                        
                        t5=row[5]
                        R5=t5-Cv5-Cfixe-DT
                        IS5=R5*0.3
                        RN5=R5-IS5
                        cf5=RN5+DT
                        CFA5=cf5*((1+c)**(-5))
                        
                        t6=row[6]
                        R6=t6-Cv6-Cfixe-DT
                        IS6=R6*0.3
                        RN6=R6-IS6
                        cf6=RN6+DT
                        CFVR=cf6+VR
                        CFA6=CFVR*((1+c)**(-6))
        
                
                CF =[(val,t1,t2,t3,t4,t5,t6),(C1,Cv1,Cv2,Cv3,Cv4,Cv5,Cv6),(C2,Cfixe,Cfixe,Cfixe,Cfixe,Cfixe,Cfixe),(value6,DT,DT,DT,DT,DT,DT),(value4,R1,R2,R3,R4,R5,R6),(value7,IS1,IS2,IS3,IS4,IS5,IS6),(value5,RN1,RN2,RN3,RN4,RN5,RN6),(value,cf1,cf2,cf3,cf4,cf5,cf6),(value2,0,0,0,0,0,CFVR),(value3,CFA1,CFA2,CFA3,CFA4,CFA5,CFA6)]

                # Exécuter la requête d'insertion dans la table de CF
                cursor.executemany('''INSERT INTO
                   CF(cf_en_KDH, n1 , n2 ,n3,n4,n5,n6 )
                  VALUES(?, ?, ?, ?,?,?,?)''', CF)
                connection.commit()
                print("Calcul est ajout de CF est bien passé !!")


        def ajouterCAHT():
                return
                
                
        #fonction de la suppression d'un cf deja ajouté:
        def supprimerCF():
                valCF=str(supcf.get())
                req='''DELETE FROM
                   CF WHERE cf_en_KDH = ?'''
                cursor.execute(req,(valCF, ))
                connection.commit()
                print("Suppression de CF bien passé !!")
                
                        
        #la fonction qui affiche les CFs enregistrés pour un projet d'investissement:
        def afficherCF():
                req3='SELECT * FROM CF'
                resultat=cursor.execute(req3)
        # tableau pour l'affichage des données de la table CF:
                lblr1=Label(fen,text="LE CF EN KDH")
                lblr1.place(x=600,y=200)
                lblr2=Label(fen,text="N1")
                lblr2.place(x=800,y=200)
                lblr3=Label(fen,text="N2")
                lblr3.place(x=900,y=200)
                lblr4=Label(fen,text="N3")
                lblr4.place(x=1000,y=200)
                lblr5=Label(fen,text="N4")
                lblr5.place(x=1100,y=200)
                lblr6=Label(fen,text="N5")
                lblr6.place(x=1200,y=200)
                lblr7=Label(fen,text="N6")
                lblr7.place(x=1300,y=200)
                vy=200
                for row in resultat:
                
                        
                        print(row[0])
                        vy=vy+40
                        lbl0=lblr1=Label(fen,text=row[0])
                        lbl0.place(x=600,y=vy)
                        lbl1=lblr1=Label(fen,text=row[1])
                        lbl1.place(x=800,y=vy)
                        lbl2=lblr1=Label(fen,text=row[2])
                        lbl2.place(x=900,y=vy)
                        lbl3=lblr1=Label(fen,text=row[3])
                        lbl3.place(x=1000,y=vy)
                        lbl4=lblr1=Label(fen,text=row[4])
                        lbl4.place(x=1100,y=vy)
                        lbl5=lblr1=Label(fen,text=row[5])
                        lbl5.place(x=1200,y=vy)
                        lbl6=lblr1=Label(fen,text=row[6])
                        lbl6.place(x=1300,y=vy)
                # print(req.fetchall())
           
        #focntion qui calcule le CF d'investissement de tout le projet:

        def calculResultat():
                sd1=0
                sd2=0
                sd3=0
                sd4=0
                sd5=0
                sd6=0

                sf1=0
                sf2=0
                sf3=0
                sf4=0
                sf5=0
                sf6=0

                VAN=0
                SommeCFA=0
                SommeDIA=0
                
                reeq1='SELECT * FROM DI WHERE di_en_KDH="DI actualisé" '
                resultat1=cursor.execute(reeq1)
                for row in resultat1:
                        
                        sd1=row[1]
                        sd2=row[2]
                        sd3=row[3]
                        sd4=row[4]
                        sd5=row[5]
                        sd6=row[6]
                
                SommeDIA=sd1+sd2+sd3+sd4+sd5+sd6

                reeq2='SELECT * FROM CF WHERE cf_en_KDH="CF actualisé" '
                resultat2=cursor.execute(reeq2)
                for row in resultat2:
                        
                        sf1=0
                        sf2=row[2]
                        sf3=row[3]
                        sf4=row[4]
                        sf5=row[5]
                        sf6=row[6]
                
                SommeCFA=sf1+sf2+sf3+sf4+sf5+sf6
        # Resultat final : Calcul de la VAN pour le juger le projet:
                VAN= SommeCFA - SommeDIA
                if VAN<0:
                        lbl1res=Label(fen,text="ATTENTION VOTRE PROJET N'EST PAS RENTABLE !!!!!!!!!!!",font=("Courier",26),bg='red',fg='green')
                        lbl1res.place(x=130,y=80)
                        lbl1res2=Label(fen,text="LA VALEUR ACTUELLE NETTE EST NEGATIVE",font=("Courier",18),bg='#FFFF00',fg='red')
                        lbl1res2.place(x=100,y=630)
                        lbl1res3=Label(fen,text=VAN,font=("Courier",18),bg='#FFFF00',fg='red')
                        lbl1res3.place(x=150,y=660)
                else:
                        lbl1res=Label(fen,text="SUPER VOTRE PROJET EST  RENTABLE !!!!!!!!!!!",font=("Courier",26),bg='green',fg='yellow')
                        lbl1res.place(x=130,y=80)
                        lbl1res2=Label(fen,text="LA VALEUR ACTUELLE NETTE EST POSITIVE",font=("Courier",18),bg='red',fg='yellow')
                        lbl1res2.place(x=100,y=630)
                        lbl1res3=Label(fen,text=VAN,font=("Courier",18),bg='red',fg='yellow')
                        lbl1res3.place(x=150,y=660)
                print(VAN)
                        


        #création de la fenetre de l'application:
        fen=Tk()
        fen.geometry("1400x1300")
        fen.title("Calcul des cashs flow de projet : ")
        fen.minsize(800,600)
        fen.iconbitmap("logo.ico")
        fen.config(background='#FFC0CB')
        lbltitre=Label(fen,text="CALCUL DE CASH FLOW DE  PROJET",font=("Courier",24),bg='#77b5fe',fg='white')
        lbltitre.pack()



        # les données de la table cash flow:

        lbl1=Label(fen,text="Entrer les charges variables N1 ")
        lbl1.place(x=50,y=150)
        cv1=Entry(fen)
        cv1.place(x=400,y=150)


        lbl2=Label(fen,text="Entrer les charges variables N2 ")
        lbl2.place(x=50,y=180)
        cv2=Entry(fen)
        cv2.place(x=400,y=180)

        lbl3=Label(fen,text="Entrer les charges variables N3")
        lbl3.place(x=50,y=210)
        cv3=Entry(fen)
        cv3.place(x=400,y=210)

        lbl4=Label(fen,text="Entrer les charges variables N4")
        lbl4.place(x=50,y=240)
        cv4=Entry(fen)
        cv4.place(x=400,y=240)

        lbl5=Label(fen,text="Entrer les charges variables N5")
        lbl5.place(x=50,y=270)
        cv5=Entry(fen)
        cv5.place(x=400,y=270)

        lbl6=Label(fen,text="Entrer les charges variables N6")
        lbl6.place(x=50,y=300)
        cv6=Entry(fen)
        cv6.place(x=400,y=300)

        lbl7=Label(fen,text="Entrer les charges fixes du projet")
        lbl7.place(x=50,y=330)
        cfixe=Entry(fen)
        cfixe.place(x=400,y=330)

        lbl8=Label(fen,text="Entrer la valeur des dotations d'amortissement")
        lbl8.place(x=50,y=360)
        dotation=Entry(fen)
        dotation.place(x=400,y=360)

        lbl9=Label(fen,text="Entrer la valeur résiduelle (VR):")
        lbl9.place(x=50,y=390)
        Vr=Entry(fen)
        Vr.place(x=400,y=390)

        lbl10=Label(fen,text="Entrer la valeur de CMPC déja calculé:")
        lbl10.place(x=50,y=420)
        Cmpc=Entry(fen)
        Cmpc.place(x=400,y=420)

        lbl11=Label(fen,text="Entrer la valeur de données a supprimées :")
        lbl11.place(x=50,y=450)
        supcf=Entry(fen)
        supcf.place(x=400,y=450)





        #bouton pour l'ajout des CF
        ajouter=Button(fen,text= "Ajouter le Cash Flow à la base", command=ajouterCAHT)
        ajouter.place(x=400,y=480)
        #bouton pour l'affichage des CF:

        afficher=Button(fen,text= "Afficher les cashs flow de ce projet",command=afficherCF)
        afficher.place(x=400,y=570)

        #bouton pour supprimer un CF :
        supprimer=Button(fen,text= "Supprimer un des données",command=supprimerCF)
        supprimer.place(x=400,y=510)


        #bouton pour le calcule de CF :

        calculer=Button(fen,text= "Calculer le CF du projet", command=calculerCF)
        calculer.place(x=400,y=540)

        calculeR=Button(fen,text= "Afficher le resultat final de l'évaluation du projet !!!!!", command=calculResultat)
        calculeR.place(x=50,y=30)
        fen.mainloop()
                

