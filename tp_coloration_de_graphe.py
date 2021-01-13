'''
    TP Graphe - Coloration de graphe  
'''

import numpy

def matrice(n):
    return numpy.zeros((n, n))

# Représentation par matrice d'adjacence
m = matrice(5)
m[0, 1] = 1
m[1, 0] = 1


# --- --- --- Exo 1
m[1, 2] = 1
m[2, 1] = 1

m[1, 3] = 1
m[3, 1] = 1

m[2, 3] = 1
m[3, 2] = 1

m[2, 4] = 1
m[4, 2] = 1

m[3, 4] = 1
m[4, 3] = 1
#

# --- --- --- Exo 2
def succ(mat, n, x):
    res = set()
    for i in range(n):
        if mat[x, i] != 0:
            res.add(i)
    return res

# --- --- --- Exo 3
def greedy_colouring(mat, n):
    # dictionnaire des couleurs
    color = dict()
    for i in range(5):
        color[i] = -1
    # coloration de chaque sommet s
    for s in range(5):
        # couleur des sommets adjacents à s
        color_next = set()
        for s2 in succ(mat, 5, s):
            color_next.add(color[s2])
        # couleur pour s
        c = 0
        while c in color_next:
            c +=1
        color[s] = c
    return color


if __name__ == '__main__':
    print(greedy_colouring(m, 5))
    
        
