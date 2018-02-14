#coding : utf-8
import io
import collections
from tkinter import *

def recherche(frame):
	frame.forget()
	
	frameRecherche = Frame(fenetre, width=550, height=250)
	frameRecherche.pack(fill=BOTH)
	rechercheNumero = Button(frameRecherche, text="Rechercher par numero", command=lambda : numero(frameRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	rechercheNumero.grid(row=1,column=5)
	
	rechercheNom = Button(frameRecherche, text="Rechercher par nom", command=lambda : enregistrement(frameRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	rechercheNom.grid(row=2,column=5)
	
	recherchePrenom = Button(frameRecherche, text="Rechercher par prenom", command=lambda : enregistrement(frameRecherche), bg="grey", activebackground="grey",font="arial", height="2")
	recherchePrenom.grid(row=3,column=5)

	boutonRetour = Button(frameRecherche, text="Retour au Menu", command=lambda : menu(frameRecherche), bg="grey", activebackground="grey", font="arial", height="2")
	boutonRetour.grid(row = 4, column=5)

def numero(frame):

	dictionnaire = {}
	fichier = open("repertoire.txt", "r")
	fichier.seek(0)

	for line in fichier :
		prenom = fichier.readline()
		numero = fichier.readline()
		dictionnaire[numero] = (line, prenom)
	frame.forget()
	frameNumero = Frame(fenetre, width=550, height=250)
	frameNumero.pack(fill=BOTH)
	labelNumero = Label(frameNumero, text='Numéro de téléphone:',fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)
	varNumero = StringVar()
	entrNumero = Entry(frameNumero, textvariable=varNumero, width=30)
	entrNumero.grid(row=2,column=4, sticky=W)
	labelNom = Label(frameNumero, text=dictionnaire.get(entrNumero),fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)

	boutonRetour = Button(frameNumero, text="Retour au Menu", command=lambda : menu(frameNumero), bg="grey", activebackground="grey", font="arial", height="2")
	boutonRetour.grid(row = 4, column=4)

def enregistrement(entr1, entr2, entr3):
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

def creationNouveauContact(frame):
	frame.forget()
	
	frameCreationNouveauContact = Frame(fenetre, width=550, height=250)
	frameCreationNouveauContact.pack(fill=BOTH)
	labelPrenom = Label(frameCreationNouveauContact, text='Prenom:',fg="white", bg="grey" )
	labelPrenom.grid(row=0,column=3, sticky=W)
	varPrenom = StringVar()
	entrPrenom = Entry(frameCreationNouveauContact, textvariable=varPrenom, width=30)
	entrPrenom.grid(row=0,column=4, sticky=W)

	labelNom = Label(frameCreationNouveauContact, text='Nom:',fg="white", bg="grey" )
	labelNom.grid(row=1,column=3, sticky=W)
	varNom = StringVar()
	entrNom = Entry(frameCreationNouveauContact, textvariable=varNom, width=30)
	entrNom.grid(row=1,column=4, sticky=W)

	labelNumero = Label(frameCreationNouveauContact, text='Numéro de téléphone:',fg="white", bg="grey" )
	labelNumero.grid(row=2,column=3, sticky=W)
	varNumero = StringVar()
	entrNumero = Entry(frameCreationNouveauContact, textvariable=varNumero, width=30)
	entrNumero.grid(row=2,column=4, sticky=W)

	boutonAjouter = Button(frameCreationNouveauContact, text="Ajouter", command=lambda : enregistrement(entrPrenom, entrNom, entrNumero), bg="grey", activebackground="grey",font="arial", height="2")
	boutonAjouter.grid(row=3,column=4)
	boutonRetour = Button(frameCreationNouveauContact, text="Retour au Menu", command=lambda : menu(frameCreationNouveauContact), bg="grey", activebackground="grey", font="arial", height="2")
	boutonRetour.grid(row = 4, column=4)


def afficher(frame):
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
	bouton1 = Button(fenetre, text="Retour au Menu", command=lambda : menu(option=2), bg="grey", activebackground="grey", font="arial", height="2")
	bouton1.grid(row = 4, column=4)
	for ligne in range(5):
	    for colonne in range(5):
    		Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)


def menu(frame):
	if frame != 1:
		frame.forget()

	menu = Frame(fenetre, width=550, height=250)
	menu.pack(fill=BOTH)
	boutonAfficher = Button(menu, text="Afficher les contacts", command=lambda : afficher(menu), bg="grey", activebackground="grey",font="arial", height="2")
	boutonAfficher.grid(row=1,column=5)
	boutonRecherche = Button(menu, text="Rechercher un contact", command=lambda : recherche(menu), bg="grey", activebackground="grey",font="arial", height="2")
	boutonRecherche.grid(row=2,column=5)
	boutonNvContact = Button(menu, text="Ajouter un nouveau contact", command=lambda : creationNouveauContact(menu), bg="grey", activebackground="grey",font="arial", height="2")
	boutonNvContact.grid(row=3,column=5)
	fenetre.mainloop()


fenetre = Tk()
fenetre.geometry('550x250')
fenetre.title("Repertoire")
menu(1)