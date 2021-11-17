
def interclassement(liste1: list[int], liste2: list[int]) -> list[int]:
    """
    Fonction qui transforme deux listes TIREES en une seule liste triée.
    :param liste1: première liste triée.
    :param liste2: deuxième liste triée.
    :return: fusion de ces deux listes en une seule liste triée.
    """
    liste = []
    liste1_taille, liste2_taille = len(liste1), len(liste2)
    indice1, indice2 = 0, 0
    while indice1 < liste1_taille and indice2 < liste2_taille:
        if liste1[indice1] < liste2[indice2]:
            liste.append(liste1[indice1])
            indice1 += 1
        else:
            liste.append(liste2[indice2])
            indice2 += 1
    print(f"J'ai interclassé {liste + liste1[indice1:] + liste2[indice2:]}")
    return liste + liste1[indice1:] + liste2[indice2:]


def tri_fusion(liste: list[int]) -> list[int]:
    if len(liste) <= 1:
        return liste
    m = len(liste) // 2
    print(f"Nous allons interclasser les liste: {liste[:m]} et {liste[m:]}")
    return interclassement(tri_fusion(liste[:m]), tri_fusion(liste[m:]))

print(tri_fusion([4, 3, 8, 2, 7, 1, 5]))