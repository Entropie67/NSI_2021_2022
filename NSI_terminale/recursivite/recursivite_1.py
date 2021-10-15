

def expo(x: float, n: int) -> float:
    """
     retourne le puissance n de a
    """
    if n == 0: # la condition d'arrêt
        print("Ici n vaut 0")
        return 1
    else:
        print(f"Ici n vaut {n}")
        return x * expo(x, n-1)

# x^n = x * x * x ... x * x * x
# x^n = x * x^(n-1)
# x^4 = x * x^3

print(expo(2, 1000))

