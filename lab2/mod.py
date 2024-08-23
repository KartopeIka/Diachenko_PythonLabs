def secondFormula (x: int, n: int) -> int:
    Z = 1
    for i in range (n):
        Z *= x
    return Z