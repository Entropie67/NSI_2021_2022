
# import random
# nombre = random.randint(1, 6)

# import random as alea
# nombre = alea.randint(1, 6)

from random import randint, choice
# from mathematiques import fonctions
from mathematiques.fonctions import factorielle
nombre = randint(1, 6)
nombre = choice([1, 4, 7])


# help(random.randint) Pour demander de l'aide sur une fonction
# help(choice)
# print(nombre)

help(factorielle)
print(factorielle(5))