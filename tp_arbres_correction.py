"""
    TP - arbres binaires 1/2
"""

class Noeud(object):
    # proprietes
    def __init__(self):
        self.val = None
        self.fg = None
        self.fd = None

    def __str__(self):
        return self.val



# -- creation des sommets
a = Noeud() # a : un objet, instance de la classe Noeud
a.val = 'A'

b = Noeud()
b.val = 'B'

c = Noeud()
c.val = 'C'

d = Noeud()
d.val = 'D'


"""
     A
  B     C
   D   E F
"""

# -- creation des arcs
a.fg = b
a.fd = c

b.fd = d


# Fonctions données
def est_feuille(s):
    if est_vide(s):
        return False
    return s.fg == None and s.fd == None

def est_vide(s):
    return s == None


# --- --- --- Exo 1
e = Noeud()
e.val = 'E'

f = Noeud()
f.val = 'F'

c.fg = e
c.fd = f

# --- --- --- Exo 2
# nombre de noeuds de l'arbre
def taille(s):
    if est_vide(s):
        return 0
    if est_feuille(s):
        return 1
    return 1 + taille(s.fg) + taille(s.fd)

print("taille:", taille(a))


# --- --- --- Exo 3
# trouver la valeur x dans l'arbre
def trouver(s, x):
    if est_vide(s):
        return False
    if s.val == x: # 'E'
        return True
    if est_feuille(s):
        return False
    return trouver(s.fg, x) \
           or trouver(s.fd, x)

print('trouver E :', trouver(a, 'E'))
print('trouver Z :', trouver(a, 'Z'))
    

# --- --- --- Exo 4
def profondeur(s):
    if est_vide(s):
        return 0
    if est_feuille(s):
        return 1
    return 1 + max(profondeur(s.fg), \
                   profondeur(s.fd))

print('profondeur :', profondeur(a))


# --- --- --- Exo 5
# Parcours prefixe
def prefixe(s):
    if est_vide(s):
        return
    print(s)
    prefixe(s.fg)
    prefixe(s.fd)

prefixe(a)

def prefixe2(s, n):
    if est_vide(s):
        return
    for i in range(1, n+1):
        print('-', end='')
    print(s)
    prefixe2(s.fg, n+1)
    prefixe2(s.fd, n+1)

prefixe2(a, 0)


# --- --- --- Exo 6
def infixe(s):
    if est_vide(s):
        return
    infixe(s.fg)
    print(s)
    infixe(s.fd)

print('parcours infixe')
infixe(a)


# --- --- --- Exo 7
# A- Tout noeud interne (i.e. non feuille), possède exactement deux successeurs
# B- Toutes les feuilles sont à la même profondeur de la racine
def propriete_A(s):
    if est_vide(s):
        return True
    if est_feuille(s):
        return True
    if not est_vide(s.fg) and not est_vide(s.fd):
        return propriete_A(s.fg) \
               and propriete_A(s.fd)
    else:
        print(s)
        # ne possede pas exactent 2 fils
        return False

def propriete_B(s):
    lst = []
    propriete_B__sous(s, 0, lst)
    # arbre vide,
    # sinon il contient au moins un noeud
    # et donc au moins une feuille
    if lst == []:
        return True
    x = lst[0]
    for i in range(1, len(lst)):
        if lst[i] != x:
            return False
    return True
    
def propriete_B__sous(s, p, lst):
    if est_vide(s):
        return
    p = p+1
    if est_feuille(s):
        lst.append(p)
    else:
        propriete_B__sous(s.fg, p+1, lst)
        propriete_B__sous(s.fd, p+1, lst)

def est_arbre_binaire_parfait(s):
    return propriete_A(s) and propriete_B(s)

print('a arbre binaire parfait :', \
      est_arbre_binaire_parfait(a))

print('d arbre binaire parfait :', \
      est_arbre_binaire_parfait(d))

print('c arbre binaire parfait :', \
      est_arbre_binaire_parfait(c))

# autre exemple
# on modifie l'arbre de racine A
# en insérant le noeud G

g = Noeud()
g.val = 'G'

"""
     A
  B     C
 G  D   E F
"""

b.fg = g

print('nouvel a :')
prefixe2(a, 0)

print('nouveau a : propriete A :', \
      propriete_A(a))
print('nouveau a : propriete B :', \
      propriete_B(a))
print('nouveau a : arbre binaire parfait :', \
      est_arbre_binaire_parfait(a))
