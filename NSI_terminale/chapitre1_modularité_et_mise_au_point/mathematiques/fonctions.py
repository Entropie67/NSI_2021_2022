
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Les standars de docstring : https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format

def factorielle(n: int) -> int:
    """
    Fonctions factorielles qui retourne la factorielle de l'entrée
    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    :param n: un nombre entier
    :return: la factorielle de l'entrée
    >>> factorielle(5)
    120
    """
    response = 1
    for i in range(2, n+1):
        response = response * i
    return response

if __name__ == "__main__":
    # execute only if run as a script
    assert factorielle(5) == 120, "Il y a un problème !"
    assert factorielle(0) == 1, "problème avec 0 !"

    print(factorielle(5))
    print("coucou tu executes directement ce fichier")
