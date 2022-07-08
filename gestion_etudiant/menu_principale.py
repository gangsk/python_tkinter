#importer les bibliotheque
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox


#Fonction Connecter
def seConnecter():
    name = txtNomUtilisateur.get()
    mdp = textMdp.get()
    if(name == "" and mdp ==""):
        messagebox.showerror("","champs incomplet")
        textMdp.delete("0","end")
        txtNomUtilisateur.delete("0","end")
    elif(name=="admin" and mdp =="admin"):
        messagebox.showinfo("","Bienvenue")
        textMdp.delete("0", "end")
        txtNomUtilisateur.delete("0", "end")
        root.destroy()
        call(["python","meConnecter.py"])

    else:
        messagebox.showwarning("","Eurreur de Connexion")
        textMdp.delete("0","end")
        txtNomUtilisateur.delete("0","end")


#Ma fenetre
root = Tk()

root.title("FENETRE DE CONNEXION")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure(background="#201D1D")

#ajouter un titre


lblTitre = Label(root,borderwidth = 3, relief = SUNKEN
                   , text ="SYSTEME D'AUTHENTIFICATION", font =("Sans Serif",15), background = "#201D1D", fg="white")
lblTitre.place(x = 0, y = 0, width=400)

lblNomUtilisateur = Label (root, text="user :", font=("Arial",14),bg="#201D1D", fg="white")
lblNomUtilisateur.place(x = 5, y= 100, width=150)
txtNomUtilisateur = Entry(root,bd=4, font=("Arial",13))
txtNomUtilisateur.place(x=150,y=100,width=200,height=30)

lblMdp = Label (root, text="password :", font=("Arial",14),bg="#201D1D", fg="white")
lblMdp.place(x = 5, y= 150, width=150)
textMdp = Entry(root,show="*",bd=4, font=("Arial",13))
textMdp.place(x=150,y=150,width=200,height=30)

#Bouton de connexion

btnEnrigistrer = Button(root, text = "Connexion", font= ("Arial",16),bg="#567CC4",fg="white",command=seConnecter)
btnEnrigistrer.place(x=150, y=200,width=200)


#execution

root.mainloop()

