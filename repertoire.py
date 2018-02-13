#coding : utf-8
import io
import collections
from tkinter import *

def recherche(fenetre, bouton1, bouton3, bouton2):
	bouton1.grid_forget()
	bouton2.grid_forget()
	bouton3.grid_forget()
	
	rechercheNumero = Button(fenetre, text="Rechercher par numero", command=lambda : numero(rechercheNumero, rechercheNom, recherchePrenom), bg="grey", activebackground="grey",font="arial", height="2")
	rechercheNumero.grid(row=1,column=5)
	
	rechercheNom = Button(fenetre, text="Rechercher par nom", command=lambda : enregistrement(rechercheNumero, rechercheNom, recherchePrenom), bg="grey", activebackground="grey",font="arial", height="2")
	rechercheNom.grid(row=2,column=5)
	
	recherchePrenom = Button(fenetre, text="Rechercher par prenom", command=lambda : enregistrement(rechercheNumero, rechercheNom, recherchePrenom), bg="grey", activebackground="grey",font="arial", height="2")
	recherchePrenom.grid(row=3,column=5)

def numero(entr1, entr2, entr3):
	entr1.grid_forget()
	entr2.grid_forget()
	entr3.grid_forget()
	dictionnaire = {}
	fichier = open("repertoire.txt", "r")
	fichier.seek(0)

	for line in fichier :
		prenom = fichier.readline()
		numero = fichier.readline()
		dictionnaire[numero] = (line, prenom)

	labelNumero = Label(fenetre, text='Numéro de téléphone:',fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)
	varNumero = StringVar()
	entrNumero = Entry(fenetre, textvariable=varNumero, width=30)
	entrNumero.grid(row=2,column=4, sticky=W)
	labelNom = Label(fenetre, text=dictionnaire.get(entrNumero),fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)

	


def enregistrement(entr1, entr2, entr3):
	print("click")
	nom = entr2.get()
	print(nom)
	prenom = entr1.get()
	numero = entr3.get()
	fichier = open("repertoire.txt","a")
	fichier.write(nom+"\n"+prenom+"\n"+numero+"\n")
	fichier.close()
	entr1.delete(0, len(prenom))
	entr2.delete(0, len(nom))
	entr3.delete(0, len(numero))

def creationNouveauContact(fenetre, bouton1, bouton3, bouton2):

	bouton1.grid_forget()
	bouton2.grid_forget()
	bouton3.grid_forget()
	
	labelPrenom = Label(fenetre, text='Prenom:',fg="white", bg="grey" )
	labelPrenom.grid(row=0,column=3, sticky=W)
	varPrenom = StringVar()
	entrPrenom = Entry(fenetre, textvariable=varPrenom, width=30)
	entrPrenom.grid(row=0,column=4, sticky=W)

	labelNom = Label(fenetre, text='Nom:',fg="white", bg="grey" )
	labelNom.grid(row=1,column=3, sticky=W)
	varNom = StringVar()
	entrNom = Entry(fenetre, textvariable=varNom, width=30)
	entrNom.grid(row=1,column=4, sticky=W)

	labelNumero = Label(fenetre, text='Numéro de téléphone:',fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)
	varNumero = StringVar()
	entrNumero = Entry(fenetre, textvariable=varNumero, width=30)
	entrNumero.grid(row=2,column=4, sticky=W)


	boutonAjouter = Button(fenetre, text="Ajouter", command=lambda : enregistrement(entrPrenom, entrNom, entrNumero), bg="grey", activebackground="grey",font="arial", height="2")
	boutonAjouter.grid(row=3,column=4)
	boutonRetour = Button(fenetre, text="Retour", command=lambda : menu(option=1, bouton1=boutonRetour, bouton2=boutonAjouter, entr1=entrPrenom, entr2=entrNumero, entr3=entrNom, label1=labelPrenom, label2=labelNumero, label3=labelNom), bg="grey", activebackground="grey", font="arial", height="2")
	boutonRetour.grid(row = 4, column=4)


def afficher(fenetre, bouton2, bouton3, bouton1):
	dictionnaire = {}
	fichier = open("repertoire.txt", "r")
	fichier.seek(0)
	n = 1
	for line in fichier :
		prenom = fichier.readline()
		numero = fichier.readline()
		bouton1.grid_forget()
	bouton1.grid_forget()
	bouton2.grid_forget()
	bouton3.grid_forget()
	bouton1 = Button(fenetre, text="Retour", command=lambda : menu(option=2), bg="grey", activebackground="grey", font="arial", height="2")
	bouton1.grid(row = 4, column=4)
	for ligne in range(5):
	    for colonne in range(5):
    		Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)


def menu(option=0, bouton1=1, bouton2= 1, bouton3= 1, entr1=1, entr2=1, entr3=1, label1=1, label2=1, label3=1):
	if option == 0:
		pass
	elif option == 1:
		bouton1.grid_forget()
		bouton2.grid_forget()
		entr1.grid_forget()
		entr2.grid_forget()
		entr3.grid_forget()
		label1.grid_forget()
		label2.grid_forget()
		label3.grid_forget()

	else:
		pass

	
	label = Label(fenetre, text="accueil")
	boutonAfficher = Button(fenetre, text="Afficher les contacts", command=lambda : afficher(fenetre, boutonNvContact, boutonAfficher, boutonRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	boutonAfficher.grid(row=1,column=5)
	boutonRecherche = Button(fenetre, text="Rechercher un contact", command=lambda : recherche(fenetre, boutonNvContact, boutonAfficher, boutonRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	boutonRecherche.grid(row=2,column=5)
	boutonNvContact = Button(fenetre, text="Ajouter un nouveau contact", command=lambda : creationNouveauContact(fenetre, boutonNvContact, boutonAfficher, boutonRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	boutonNvContact.grid(row=3,column=5)
	fenetre.mainloop()




fenetre = Tk()
fenetre.geometry('550x250')
fenetre.title("Repertoire")
menu()