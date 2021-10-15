
def expo(a: int, b: int, n: int) -> int:
    """
    fonction qui retourne le reste de division de a puissance b par n
    :param a: entier dont on prend la puissance
    :param b: exposant
    :param n: diviseur
    :return: le reste dans la division par n de a^b

    >>> expo(53, 2, 2) # 53 ^ 2 [2]
    1

    """
    return a ** b % n


assert expo(2, 3, 7) == 1
assert expo(2, 5, 5) == 2


def pgcd(a: int, b: int) -> int:
    """
    Fonction qui retourne le PGCD de a et b
    :param a: premier entier
    :param b: deuxième entier
    :return: pgcd de a et b
    """
    if a < b:
        a, b = b, a
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a


assert pgcd(1578, 534) == 6
assert pgcd(534, 1578) == 6
assert pgcd(143, 149) == 1


def is_prime(n: int) -> bool:
    """
    indique si un enter est premier
    :param n: l'entier dont on test la primalité
    :return: vrai ou faux
    """
    if n == 2:
        return True
    for i in range(3, int(n ** (1/2)), 2):
        if n % i == 0:
            return False
    return True


def decomposition(n: int) -> list[tuple[int]]:
    """
    Fonction qui retourne la décomposition en facteurs premiers de n.
    :param n:
    :return: la décomposition sous la forme [(facteur, multiplicité), ...]
    """
    liste_facteurs = []
    if is_prime(n):
        liste_facteurs.append((n, 1))
        return liste_facteurs
    j = 2
    while n > 1:
        if n % j == 0:
            liste_facteurs.append(j)
            n //= j
        else:
            j += 1
    return liste_facteurs

print(decomposition(2356))

