n=20
sum = 0
string = 'n    y\n'
for i in range(1, n+1):
    y = 2*i-1
    sum += y
    if(i<10):
        string += str(i) + ' ' * 4 + str(y) + 'x\n'
    else:
        string += str(i) + ' ' * 3 + str(y) + 'x\n'
print(string,"Sum of elements: ", sum, "x")