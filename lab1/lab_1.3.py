N=int(input("Input N in a range from 2 to 9: "))
while(N<2 or N>9):
    N = int(input("You made a mistake. Please input N in a range from 2 to 9: "))
string = ""
for i in range(N, 0, -1):
    string += '  ' * (N - i) + (str(N) + ' ') * i + '\n'
for i in range(1, N+1):
    string += '  ' * (N - i) + (str(N) + ' ') * i + '\n'
print(string)