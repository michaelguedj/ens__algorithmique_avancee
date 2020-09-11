
''' sur les graphes '''

class Noeud(object):
    # proprietes
    def __init__(self):
        self.val = 'empty'
        self.succ = [] # list des successeurs

    # methodes
    def add(self, x):
        if x not in self.succ:
            self.succ.append(x)
        #else:
        #    print("deja present")

    def __str__(self):
        res = "val: " + self.val
        for x in self.succ:
            res +=  "\n-->" + x.val
        return res

    
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


"""
     a->b
     a->c
     a->d

     b->a
     b->e
     
     c->e
     c->d

     d->a
     d->e
  
"""

# -- creation des arcs
a.add(b)
a.add(c)
a.add(d)

b.add(a)
b.add(e)

c.add(e)
c.add(d)

d.add(a)
d.add(e)

