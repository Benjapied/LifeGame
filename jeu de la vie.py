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
 
tab = plateau(4)
 
def displayTable(tab):
    for i in tab:
        print(i)

tab[0][1] = 'X'
 
displayTable(tab)
 
 
#Fontion qui vérifie si il y a un X au dessus de la case selectionée en paramètre
def checkUp (tab,x,y):
  if y == 0 :
    return None
  else :
    return tab[x-1][y]
 
#Fontion qui vérifie si il y a un X a gauche de la case selectionée en paramètre
def checkLeft (tab,x,y):
  if x == 0 :
    return None
  else :
    return tab[x][y-1]
 
#Fontion qui vérifie si il y a un X a droite de la case selectionée en paramètre
def checkRight (tab,x,y):
  if x == len(tab) :
    return None
  else :
    return tab[x][y+1]
 
#Fontion qui vérifie si il y a un X en dessous de la case selectionée en paramètre
def checkDown (tab,x,y):
  if y == len(tab):
    return None
  else :
    return tab[x+1][y]
 
def checkState (tab,x,y) :
  #liste qui contient les cases adjascentes dans cet ordre Haut, Bas, Gauche, Droite
  l = []
  l.append(checkUp(tab,x,y))
  l.append(checkDown(tab,x,y))
  l.append(checkLeft(tab,x,y))
  l.append(checkRight(tab,x,y))
  return l
 
 
print(checkState(tab,1,1))
print(checkUp(tab,1,1))
print(checkDown(tab,1,1))
ds