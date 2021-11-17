
def compte_voyelles(text: str) -> int:
    voyelles = "aeiouy"
    compteur = 0
    for lettre in text:
        if lettre in voyelles:
            compteur += 1
    print(compteur)

compte_voyelles("Coucou")