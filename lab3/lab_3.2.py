word = str(input("Input any word: "))
isPalindrome: bool = True
for i in range(len(word)//2+1):
    if (word[i] != word[-i-1]):
        isPalindrome = False
        break
if (isPalindrome):
    print("That word is palindrom")
else:
    print("That word is not palindrom")