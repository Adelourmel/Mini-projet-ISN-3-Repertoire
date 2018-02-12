#coding : utf-8
import io
import collections
from tkinter import *

def recherche():
	pass
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

def creationNouveauContact():

	label = Label(fenetre, text="creationNouveauContact")
	label1 = Label(fenetre, text='Prenom:',fg="white", bg="grey" )
	label1.grid(row=0,column=3, sticky=W)
	varPrenom = StringVar()
	entr1 = Entry(fenetre, textvariable=varPrenom, width=30)
	entr1.grid(row=0,column=4, sticky=W)


	label1 = Label(fenetre, text='Nom:',fg="white", bg="grey" )
	label1.grid(row=1,column=3, sticky=W)
	varNom = StringVar()
	entr2 = Entry(fenetre, textvariable=varNom, width=30)
	entr2.grid(row=1,column=4, sticky=W)



	label1 = Label(fenetre, text='Numéro de téléphone:',fg="white", bg="grey" )
	label1.grid(row=2,column=3, sticky=W)
	varNumero = StringVar()
	entr3 = Entry(fenetre, textvariable=varNumero, width=30)
	entr3.grid(row=2,column=4, sticky=W)


	bouton4 = Button(fenetre, text="Ajouter", command=lambda : enregistrement(entr1, entr2, entr3), bg="grey", activebackground="grey",font="arial", height="2")
	bouton4.grid(row=3,column=4)


def afficher():
	dictionnaire = {}
	fichier = open("repertoire.txt", "r")
	fichier.seek(0)
	for line in fichier :
		prenom = fichier.readline()
		numero = fichier.readline()
		print(line + prenom + numero)
		dictionnaire[line] = (prenom, numero)
	dictionnaire = collections.OrderedDict(sorted(dictionnaire.items(), key=lambda t: t[0]))
	print(dictionnaire)
	fichier.close()




fenetre = Tk()
fenetre.geometry('550x250')
fenetre.title("Repertoire")
label = Label(fenetre, text="accueil")
bouton1 = Button(fenetre, text="Afficher les contacts", command=afficher, bg="grey", activebackground="grey",font="arial", height="2")
bouton1.grid(row=1,column=5)
bouton3 = Button(fenetre, text="Rechercher un contact", command=recherche, bg="grey", activebackground="grey",font="arial", height="2")
bouton3.grid(row=2,column=5)
bouton2 = Button(fenetre, text="Ajouter un nouveau contact", command=creationNouveauContact, bg="grey", activebackground="grey",font="arial", height="2")
bouton2.grid(row=3,column=5)



fenetre.mainloop()

