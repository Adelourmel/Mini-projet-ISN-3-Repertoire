#coding : utf-8

def recherche():
	pass	

def creationNouveauContact():
	nom=input("Nom du contact: ")
	prenom=input("Prenom du contact: ")
	numero=input("Numero du contact: ")
	fichier=open("repertoire.txt","w")
	fichier.write(nom,prenom,numero)
	fichier.close
def afficher():
	pass

