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
 
tab = plateau(5)

def displayTable(tab):
    for i in tab:
        print(i)
 
displayTable(tab)
 
 
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
  #liste qui contient les cases autour
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
  count = 0
  for i in range(len(liste)-1) :
    if liste[i] == 1 :
      count = count + 1
  return count

def checkLife (tab,x,y) :
  if checkAround(checkState(tab,x,y)) == 2 :
    return
  if checkAround(checkState(tab,x,y)) == 3 :
    tab[x][y] = 1 
  else :
    tab[x][y] = 0


def fullCheck (tab) :
  for i in range (len(tab)) :
    for j in range (len(tab)) :
      checkLife (tab,i,j)

fullCheck(tab)

print("\n")
displayTable(tab)

fullCheck(tab)

print("\n")
displayTable(tab)

print(checkUp(tab,1,1))
print(checkDown(tab,1,1))
print(checkRight(tab,0,4))