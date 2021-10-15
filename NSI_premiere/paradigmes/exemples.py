
class Hero:

    def __init__(self, name): # C'est une méthode, celle ci est le constructeur
        self.name = name # attribut
        self.hp = 100
        self.force = 700

wanda = Hero("wanda")
loki = Hero("loki")

class Boite:

    def __init__(self, ouvert=False):
        self._ouvert = ouvert

    def ouvre(self):
        self._ouvert = True

    def ferme(self):
        self._ouvert = False

    def __str__(self):
        phrase = "C'est une boite qui est"
        phrase += " ouverte" if self._ouvert == True else " fermée"
        return phrase

boite1 = Boite()
boite2 = Boite()
boite3 = Boite(True)

boite1.ouvre()
boite1.ferme()
print(boite1)
boite1.ouvre()
print(boite1)

def f(n):
    def g(m):
        return m ** n
    return g

j = f(5)
print(f(3)(2))