
# n! = n * (n-1) * (n-2) * ... * 2 * 1

def factorielle(n: int) -> int:

    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


def inverse(lst):
    if len(lst) == 1:
        return [lst[0]]
    return inverse(lst[1:]) + [lst[0]]


print(inverse([1, 2, 3, 4, 5]))