size = int(input("Введіть розмір масиву: "))
masiv = [int(input("Введіть елемент "+str(i)+": "))for i in range(size)]
odd_numbers_product = 1
check = 0
for element in masiv:
    if element%2!=0:
        odd_numbers_product*=element
        check = 1
if check:
    print(masiv,"\nДобуток непарних чисел =", odd_numbers_product)
else:
    print(masiv,"\nДаний масив не містить непарних чисел")