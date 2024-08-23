import math

def firstFormula (alpha: int) -> float:
    z = math.tan(3*alpha)
    return z
def secondFormula (x: int, n: int) -> int:
    Z = 1
    for i in range (n):
        Z *= x
    return Z

alpha = int(input("Input alpha: "))
print('\033[93m',"tan(3*alpha) = ", firstFormula(alpha), '\033[0m')

x = int(input("Input x: "))
n = int(input("Input n>=0: "))
while n<0:
    n = int(input("You made a mistake. Input n>=0: "))
print('\033[93m',"x^n = ", secondFormula(x, n), '\033[0m')