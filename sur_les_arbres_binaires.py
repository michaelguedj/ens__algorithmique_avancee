
''' sur les arbres binaires '''

class Noeud(object):
    # proprietes
    def __init__(self):
        self.val = "empty"
        self.fils_gauche = None
        self.fils_droit = None

    # methode
    def est_feuille(self):
        return self.fils_gauche == None \
               and self.fils_droit == None

# exemple
# -- creation des sommets
a = Noeud() # a : un objet, instance de la classe Noeud
a.val = 'A'

b = Noeud()
b.val = 'B'

c = Noeud()
c.val = 'C'

d = Noeud()
d.val = 'D'

e = Noeud()
e.val = 'E'

f = Noeud()
f.val = 'F'

"""
     A
  B     C
   D   E F
"""

# -- creation des arcs
a.fils_gauche = b
a.fils_droit = c

b.fils_droit = d

c.fils_gauche = e
c.fils_droit = f


# tester si le sommet est nul (arbre vide)
# fonction
def est_vide(s):
    return s == None


# nombre de noeuds de l'arbre
def taille(s):
    if est_vide(s):
        return 0
    if s.est_feuille():
        return 1
    return 1 + taille(s.fils_gauche) \
           + taille(s.fils_droit)

print("taille:", taille(a))


# trouver la valeur x dans l'arbre
def trouver(s, x):
    if est_vide(s):
        return False
    if s.val == x: # 'E'
        return True
    if s.est_feuille():
        return False
    return trouver(s.fils_gauche, x) \
           or trouver(s.fils_droit, x)


print("trouver E", trouver(a, 'E'))
print("trouver Z", trouver(a, 'Z'))


'''
ATTENTION:
la classe Noeud ne nous contraint pas a definir
necessairement des arbres binaires
'''
