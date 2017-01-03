#@ calculatrice
#@ 01/01/2017
#@ jean

# module Import


# fonction and variable creation

# body script

# bouton de sortie

# On importe Tkinter


from tkinter import *

fenetre = Tk()

operation = 0
nbre1 = 0
nbre2 = 2

print (" calculator")
print (" ")
print (" veuillez_choisir_l'operation")
print (" ")
print ("1.addition")
print (" ")
print ("2.soustraction ")
print (" ")
print ("3.multiplication ")
print (" ")
print ("4.division")


operation = input()

nbre1 = input("entrez le premier chiffre ")
nbre2 = input("entrez le deuxieme chiffre ")

if (operation == 1):
   print (nbre1 + nbre2)
elif operation == 2:
   print (nbre1 - nbre2)
elif operation == 3:
   print (nbre1 * nbre2)
elif operation == 4:
   print (nbre1 / nbre2)
