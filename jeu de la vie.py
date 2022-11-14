import random as r

#Fonction qui va créer un plateau carré de longueur x
def plateau (x):
  tab = []
  tab2 = []
  for j in range (x) :
    tab = []
    for i in range (x) :
      tab.append(r.randint(0,1))
    tab2.append(tab)
  return tab2

def displayTable(tab):
    for i in tab:
        print(i)
 

 
#Fontion qui vérifie si il y a un X au dessus de la case selectionée en paramètre
def checkUp (tab,x,y):
  if x == 0 :
    return None
  else :
    return tab[x-1][y]
 
#Fontion qui vérifie si il y a un X a gauche de la case selectionée en paramètre
def checkLeft (tab,x,y):
  if y == 0 :
    return None
  else :
    return tab[x][y-1]
 
#Fontion qui vérifie si il y a un X a droite de la case selectionée en paramètre
def checkRight (tab,x,y):
  if y == (len(tab)-1) :
    return None
  else :
    return tab[x][y+1]
 
#Fontion qui vérifie si il y a un X en dessous de la case selectionée en paramètre
def checkDown (tab,x,y):
  if x == (len(tab)-1):
    return None
  else :
    return tab[x+1][y]

#Fontion qui vérifie ce qu'il y a au dessus à gauche de la case selectionée en paramètre
def checkUpLeft (tab,x,y):
  if y == 0 or x == 0:
    return None
  else :
    return tab[x-1][y-1]

#Fontion qui vérifie ce qu'il y a au dessus à droite de la case selectionée en paramètre
def checkUpRight (tab,x,y):
  if y == (len(tab)-1) or x == 0:
    return None
  else :
    return tab[x-1][y+1]

#Fontion qui vérifie ce qu'il y a au dessous à gauche de la case selectionée en paramètre
def checkDownLeft (tab,x,y):
  if x == (len(tab)-1) or y == 0:
    return None
  else :
    return tab[x+1][y-1]

#Fontion qui vérifie ce qu'il y a au dessous à droite de la case selectionée en paramètre
def checkDownRight (tab,x,y):
  if y == (len(tab)-1) or x == (len(tab)-1):
    return None
  else :
    return tab[x+1][y+1]
 
def checkState (tab,x,y) :
  '''Fonction qui va ajouter dans une liste les cellules à proximité de la cellule ciblé'''
  l = []
  l.append(checkUpLeft(tab,x,y))
  l.append(checkUp(tab,x,y))
  l.append(checkUpRight(tab,x,y))
  l.append(checkRight(tab,x,y))
  l.append(checkDownRight(tab,x,y))
  l.append(checkDown(tab,x,y))
  l.append(checkDownLeft(tab,x,y))
  l.append(checkLeft(tab,x,y))
  return l
 
def checkAround (liste) :
  '''Fonction qui va compter le nombre de 1 qu'il y a autour d'une cellule'''
  count = 0
  for i in range(len(liste)) :
    if liste[i] == 1 :
      count = count + 1
  return count


def checkLife (tab,x,y,tab2) :
  '''Fonction qui modifie une cellule en fonction des cellules autours d'elles'''
  if checkAround(checkState(tab,x,y)) == 2 :
    tab2 [x][y] = tab[x][y]
  if checkAround(checkState(tab,x,y)) == 3 :
    tab2[x][y] = 1 
  else :
    tab2[x][y] = 0


def fullCheck (tab) :
  '''fonction qui va appliquer la modification de cellule à tout le tableau'''
  tab2 = plateau(len(tab))
  for i in range (len(tab)) :
    for j in range (len(tab)) :
      checkLife (tab,i,j,tab2)
  return tab2

tab = plateau(15)

displayTable(tab)
print('\n')

'''for i in range (5) :
  for y in range (5) :
    print(checkState(tab,i,y))
    print(checkAround(checkState(tab,i,y)))'''

for i in range (10) :
  tab = fullCheck(tab)
  displayTable(tab)
  print("\n")

