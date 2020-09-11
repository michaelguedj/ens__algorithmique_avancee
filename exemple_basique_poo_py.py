''' exemple basique POO Python '''

class Personne(object):
    # proprietes
    def __init__(self):
        self.nom = "empty"
        self.prenom = "empty"
        self.age = -1

    # methode    
    def frequence_cardiaque_maximale(self):
        return 220 - self.age
   
        
p1 = Personne() # p1 : un objet, instance de la classe Personne
print(p1.nom, p1.prenom, p1.age) #~~> empty, empty, -1

print("---")

p1.nom = "Bond"
p1.prenom = "James"
p1.age = 40
print(p1.nom, p1.prenom, p1.age) #~~> Bond James 40
print(p1.frequence_cardiaque_maximale()) #~~> 180 (220-40)
