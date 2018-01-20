#coding : utf-8

def recherche():
	pass

def creationNouveauContact():
	nom = input("Nom du contact: ")
	prenom = input("Prenom du contact: ")
	numero = input("Numero du contact: ")
	fichier = open("repertoire.txt","a")
	fichier.write(nom+" "+prenom+" "+numero+"\n")
	fichier.close

def afficher():
	fichier = open("repertoire.txt", "r")
	lecture = fichier.read()
	print(lecture)


choix = ""
while choix != "4" :
	print("Vous souhaitez :\n1. Créer un nouveau contact\n2. Afficher les contacts\n3. Rechercher un contact\n4. Quitter")
	choix = input("Entrez votre choix : ")
	if choix == "1":
		creationNouveauContact()
	elif choix == "2":
		afficher()
	elif choix == "3":
		recherche()
	elif choix == "4":
		pass
	else :
		print("Erreur de saisie")

