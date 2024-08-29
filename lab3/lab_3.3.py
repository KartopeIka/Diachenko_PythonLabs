import re

superString = str(input("Ввведіть речення: "))
superString = superString.replace('"', '').replace('.', '').replace('?', '').replace(',', '')
superString = superString.lower()
splittedString = superString.split(" ")

finalString = "Слова, які починаються з 'як': "
for i in range(len(splittedString)):
    find = re.match('як'or 'Як', splittedString[i])
    if find:
        finalString += splittedString[i] + " "
print(finalString)