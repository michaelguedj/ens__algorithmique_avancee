"""
    TP - arbres binaires 2/2
"""

class Noeud(object):
    # proprietes
    def __init__(self):
        self.val = None
        self.fg = None
        self.fd = None

    def __str__(self):
        return str(self.val)

# -- creation des sommets
a = Noeud() # a : un objet, instance de la classe Noeud
a.val = 5

b = Noeud()
b.val = 2

c = Noeud()
c.val = 8


f = Noeud()
f.val = 9

"""
     A
  B     C
 G D   E F
"""

# -- creation des arcs
a.fg = b
a.fd = c

c.fd = f


# Fonctions données
# tester si le sommet est nul (arbre vide)
# fonction
def est_feuille(s):
    if est_vide(s):
        return False
    return s.fg == None \
           and s.fd == None

def est_vide(s):
    return s == None


# --- --- --- Exo 1
g = Noeud()
g.val = 1

d = Noeud()
d.val = 3

e = Noeud()
e.val = 8

b.fg = g
b.fd = d

c.fg = e


# --- --- --- Exo 2
def somme(s):
    if est_vide(s):
        return 0
    if est_feuille(s):
        return s.val
    return s.val + somme(s.fg) + somme(s.fd)

print('somme :', somme(a))   


# --- --- --- Exo 3
def est_abr(s):
    if est_vide(s):
        return True
    if est_feuille(s):
        return True
    if not est_vide(s.fg):
        if not(s.fg.val <= s.val):
            return False
    if not est_vide(s.fd):
        if not(s.val < s.fd.val):
            return False
    return est_abr(s.fg) and est_abr(s.fd)

print('est_abr :', est_abr(a))
e.val = 10
print('est_abr :', est_abr(a))
e.val = 8   # retour "à la normale"


# --- --- --- Exo 4
def rcc_abr(s, x):
    if est_vide(s):
        return False
    if x == s.val:
        return True 
    if x < s.val:
        return rcc_abr(s.fg, x)
    return rcc_abr(s.fd, x)

print('rcc_abr 3:', rcc_abr(a, 3))
print('rcc_abr 10:', rcc_abr(a, 10))


# --- --- --- Exo 5
# infixe abr
def infixe(s):
    if est_vide(s):
        return
    infixe(s.fg)
    print(s)
    infixe(s.fd)
    
infixe(a)
