
def recherche(liste: list[int], element: int) -> bool:
    if len(liste) == 0:
        return False
    m = len(liste) // 2
    if liste[m] == element:
        return True
    elif liste[m] < element:
        return recherche(liste[m + 1:], element)
    else:
        return recherche(liste[:m], element)

print(recherche([1, 3, 6, 8, 12], 3))