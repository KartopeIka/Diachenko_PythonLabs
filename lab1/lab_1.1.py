a=int(input("Input 'a' in a range from 1 to 100: "))
while(a<1 or a>100):
    a = int(input("You made a mistake. Please input 'a' in a range from 1 to 100: "))
b=int(input("Input 'b' in a range from 1 to 100: "))
while(b<1 or b>100):
    b = int(input("You made a mistake. Please input 'b' in a range from 1 to 100: "))
if a>b:
    result=a/b+1
elif a==b:
    result=a+25
else:
    result=(a*b-2)/b
print("Result: ", result)