'''
    TP Graphe - Parcours en Largeur  
'''

import numpy

# Représentation par liste d'adjacence
succ = [None]*5
succ[0] = [1, 3]

succ[1] = [0, 2, 3]
succ[2] = [1, 2, 3]
succ[3] = [0, 1, 2, 4]
succ[4] = [3]

class File(object):
    # proprietes
    def __init__(self):
        self.ct = []

    def est_vide(self):
        return self.ct == []

    def taille(self):
        return len(self.ct)

    def enfiler(self, x):
        self.ct = [x] + self.ct

    def defiler(self):
        if self.est_vide():
            return None
        return self.ct.pop()
    
    def __str__(self):
        return str(self.ct)

def bfs(succ, s_0):
    done = [ s_0 ]
    todo = File()
    todo.enfiler( s_0 )
    while not todo.est_vide():
        s = todo.defiler()
        for s_ in succ[s]:
            if not(s_ in done):
                todo.enfiler( s_ )
                done = done + [ s_ ]
    return done


if __name__ == '__main__':
    # test File
    f = File()
    print('f vide ?', f.est_vide())
    print(f)
    f.enfiler(1)
    print(f)
    f.enfiler(2)
    print(f)
    f.enfiler(3)
    print(f)
    print('defiler', f.defiler())
    print(f)
    print('defiler', f.defiler())
    print(f)
    print('defiler', f.defiler())
    print(f)
    print('defiler', f.defiler())
    print(f)

    print('BFS(succ, 0) :')
    print(bfs(succ, 0))
    
    print('BFS(succ, 1) :')
    print(bfs(succ, 1))

    print('BFS(succ, 4) :')
    print(bfs(succ, 4))
