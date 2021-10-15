# 0 1 1 2 3 5 8 13 21

def fibo(n: int) -> int:
    """
    Retourne la valeur au rang n de la suite de fibonacci
    :param n: indice de la valeur souhaitée
    :return: valeur associée à l'indice
    """
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)



# fibo avec mémoïsation

def fibo_memo(n: int) -> int:
    memo = dict() #pour mémoriser les différentes valeurs
    def fib(n: int) -> int:
        if n in memo:
            return memo[n]
        if n < 2:
            memo[n] = n
        else:
            memo[n] = fib(n -1) + fib(n - 2)
        return memo[n]
    return fib(n)

# print(fibo(37))
print(fibo_memo(50))

# https://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation
