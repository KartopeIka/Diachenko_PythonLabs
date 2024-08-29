superString = str(input("Input any sentence: "))
splittedString = superString.split(" ")
finalString = "Result: "
for i in range(len(splittedString)):
    finalString += splittedString[i][:len(splittedString[i])//2] + " "
print(finalString)