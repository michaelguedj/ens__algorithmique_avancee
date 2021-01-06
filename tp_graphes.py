'''
    TP Graphe non orienté 
'''
import numpy

def matrice(n):
    return numpy.zeros((n, n))

# Représentation par matrice d'adjacence
m = matrice(6)
m[0, 1] = 1

# Représentation par liste d'adjacence
succ = [None]*5
succ[0] = [1, 3]

# --- --- --- Exo 1
# Représentation par matrice d'adjacence
m[0, 3] = 1
m[3, 0] = 1

m[1, 2] = 1
m[2, 1] = 1
m[1, 3] = 1
m[3, 1] = 1

m[2, 2] = 1
m[2, 3] = 1
m[3, 2] = 1

m[3, 4] = 1
m[4, 3] = 1

# --- --- --- Exo 2
# Représentation par liste d'adjacence
succ[1] = [0, 2, 3]
succ[2] = [1, 2, 3]
succ[3] = [0, 1, 2, 4]
succ[4] = [3]

# --- --- --- Exo 3
# Tester l'existence d'un arc
def est_arc__mat(mat, s1, s2):
    return mat[s1, s2] != 0

def est_arc__lst(lst, s1, s2):
    for x in lst[s1]:
        if x == s2:
            return True
    return False

print('-- EXO 3 --')
print('1-3', est_arc__mat(m, 1, 3))
print('0-2', est_arc__mat(m, 0, 2))

print('1-3', est_arc__lst(succ, 1, 3))
print('0-2', est_arc__lst(succ, 0, 2))

# --- --- --- Exo 4
# Retourner les sommets adjacents à un sommet
def sommets_adjacents__mat(mat, n, s):
    res = []
    for i in range(n):
        if mat[s, i] != 0:
            res.append(i)
    return res

def sommets_adjacents__lst(lst, s):
    return lst[s]

print('-- EXO 4 --')
print('adjacents(3)=',
      sommets_adjacents__mat(m, 5, 3))
print('adjacents(3)=',
      sommets_adjacents__lst(succ, 3))

# --- --- --- Exo 5
# Parcourir l'ensemble des arcs
def parcours__mat(mat, n):
    for j in range(n):
        for i in range(j+1):
            if mat[i, j] != 0:
                print((i, j))
    print()

def parcours__lst(lst, n):
    for i in range(n):
        for j in lst[i]:
            print((i, j))
    print()

# parcours__lst sans répétition
def parcours__lst_2(lst, n):
    res = []
    for i in range(n):
        for j in lst[i]:
            if not ( (i, j) in res ) \
               and not ( (j, i) in res ):
                res.append((i, j))
    print(res)



print('-- EXO 5 --')
parcours__mat(m, 5)
parcours__lst(succ, 5)
parcours__lst_2(succ, 5)
