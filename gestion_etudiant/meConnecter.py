#importation des blibotheque
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector


def Ajouter():
    NumeroCarteEtudiant = textNumeroCarteEtudiant.get()
    nom = txtNom.get()
    prenom = txtPrenom.get()
    anneeNaissance = txtAnnee.get()
    filiere = txtFiliere.get()
    departement = txtDepartement.get()
    anneeInscription= txtAnneInscription.get()
    moyenne  =  txtmoyenne.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO etudiant (numero,nom,prenom,anneeNaissance,filiere,departement,anneeIns,moyenne) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (NumeroCarteEtudiant,nom,prenom,anneeNaissance,filiere,departement,anneeInscription,moyenne)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereNumero = meConnect.lastrowid
        messagebox.showinfo("information","information ajouter")
        root.destroy()
        call(["python","meConnecter.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def Modifier():
    NumeroCarteEtudiant = textNumeroCarteEtudiant.get()
    nom = txtNom.get()
    prenom = txtPrenom.get()
    anneeNaissance = txtAnnee.get()
    filiere = txtFiliere.get()
    departement = txtDepartement.get()
    anneeInscription = txtAnneInscription.get()
    moyenne = txtmoyenne.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_eleve")
    meConnect = maBase.cursor()


    try:
        sql = "update etudiant set nom= %s,prenom= %s,anneeNaissance= %s,filiere= %s,departement= %s,departement= %s,moyenne= %s where numero= %s"
        val = ( nom, prenom, anneeNaissance, filiere, departement, anneeInscription, moyenne,NumeroCarteEtudiant)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereNumero = meConnect.lastrowid
        messagebox.showinfo("information", "information modifier")
        root.destroy()
        call(["python", "meConnecter.py"])
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def Supprimer():
    NumeroCarteEtudiant = textNumeroCarteEtudiant.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "delete from etudiant where numero = %s"
        val = (NumeroCarteEtudiant,)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereNumero = meConnect.lastrowid
        messagebox.showinfo("information", "information Supprimer")
        root.destroy()
        call(["python", "meConnecter.py"])

    except Exception as e:
        print(e)
        # retour
        maBase.rollback()
        maBase.close()



#Ma fenetre
root = Tk()

root.title("MENU PRINCIPALE")
root.geometry("1290x700+0+0")
root.resizable(False,False)
root.configure(background="#201D1D")

#Ajouter le titre
lblTitre = Label(root,borderwidth=3,relief=SUNKEN
                 , text= " SYSTEME DE GESTION D'ETUDIANTS",font=("Sans Serif",25), background="#567CC4",fg="#FFFAFA")
lblTitre.place(x=0 , y=0, width=1350,height=100)

#Detail des eleves
#Numero de Carte Etudiant
lblNumeroCarteEtudiant = Label(root,text="numéro carte d’étudiant",font=("Arial",18),bg="#201D1D",fg="white")
lblNumeroCarteEtudiant.place(x=10, y=140,width=270)
textNumeroCarteEtudiant = Entry(root,bd=4,font=("Arial",14))
textNumeroCarteEtudiant.place(x=300, y=140,width=150)

#NOM

lblNom = Label(root,text="nom",font=("Arial",18),bg="#201D1D",fg="white")
lblNom.place(x=10, y=200,width=270)
txtNom = Entry(root,bd=4,font=("Arial",14))
txtNom.place(x=300, y=200,width=230)

#prenom
lblPrenom = Label(root,text="prenom",font=("Arial",18),bg="#201D1D",fg="white")
lblPrenom.place(x=10, y=260,width=270)
txtPrenom = Entry(root,bd=4,font=("Arial",14))
txtPrenom.place(x=300, y=260,width=230)

#Annee de naissance
lblAnnee = Label(root,text="année de naissance",font=("Arial",18),bg="#201D1D",fg="white")
lblAnnee.place(x=10, y=320,width=270)
txtAnnee = Entry(root,bd=4,font=("Arial",14))
txtAnnee.place(x=300, y=320,width=150)

#Filiere
lblFiliere = Label(root,text="filière",font=("Arial",18),bg="#201D1D",fg="white")
lblFiliere.place(x=10, y=380,width=270)
txtFiliere = Entry(root,bd=4,font=("Arial",14))
txtFiliere.place(x=300, y=380,width=230)

#departement
lblDepartement = Label(root,text="département",font=("Arial",18),bg="#201D1D",fg="white")
lblDepartement.place(x=10, y=440,width=270)
txtDepartement = Entry(root,bd=4,font=("Arial",14))
txtDepartement.place(x=300, y=440,width=230)

#année d’inscription
lblAnneInscription = Label(root,text="année d’inscription",font=("Arial",18),bg="#201D1D",fg="white")
lblAnneInscription.place(x=10, y=510,width=270)
txtAnneInscription = Entry(root,bd=4,font=("Arial",14))
txtAnneInscription.place(x=300, y=510,width=150)
# moyenne
lblmoyenne = Label(root,text="moyenne",font=("Arial",18),bg="#201D1D",fg="white")
lblmoyenne.place(x=10, y=570,width=270)
txtmoyenne = Entry(root,bd=4,font=("Arial",14))
txtmoyenne.place(x=300, y=570,width=150)

#Button Enrigistrer
btnEnrigistrer = Button(root, text="Enrigistrer", font= ("Arial",16),bg="#5B61B9",fg="white",command=Ajouter)
btnEnrigistrer.place(x=300, y=630,width=200)

#Button modifier
btnModifier = Button(root, text="Modifier", font= ("Arial",16),bg="#7C4AD2",fg="white",command=Modifier)
btnModifier.place(x=510, y=630,width=200)

#Button Supprimer
btnSupprimer = Button(root, text="Supprimer", font= ("Arial",16),bg="#D63D3D",fg="white",command=Supprimer)
btnSupprimer.place(x=720, y=630,width=200)
#table
table = ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8), height=50, show="headings")
table.place(x=550, y=150 , width=710,height=475)
#Entete
table.heading(1, text = "NUMERO")
table.heading(2, text = "NOM")
table.heading(3, text = "PRENOM")
table.heading(4, text = "ANNEE DE NAISSANCE")
table.heading(5, text = "FILIERE")
table.heading(6, text = "DEPARTEMENT")
table.heading(7, text = "ANNEE D'INSCRIPTION")
table.heading(8, text = "MOYENNE")
#Definir les dimensions des colones

table.column(1,width=10)
table.column(2,width=20)
table.column(3,width=11)
table.column(4,width=80)
table.column(5,width=30)
table.column(6,width=50)
table.column(7,width=80)
table.column(8,width=20)

#afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_eleve")
meConnect = maBase.cursor()
meConnect.execute("select * from etudiant")
for row in meConnect:
    table.insert('',END,values=row)
maBase.close()


#execution

root.mainloop()