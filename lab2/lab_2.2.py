from mod import secondFormula

x = int(input("Input x: "))
n = int(input("Input n>=0: "))
while n<0:
    n = int(input("You made a mistake. Input n>=0: "))
print('\033[93m',"x^n = ", secondFormula(x, n), '\033[0m')