import re

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened for '", mode,"'!")
        return file


first_file_name = 'TF22_1.txt'
second_file_name = 'TF22_2.txt'
first_file = open_file(first_file_name, "w+")
#Якщо у файлі вжу щось є - очищуємо файл
if first_file != 0:
    first_file.truncate()
#додаємо записи до першого файлу
first_file.write("Sobaka kusaka\n"
                 "Why am I so hungry?\n"
                 "Murka, Masia and Bonya love eating")
print("Information was succesfully added to TF22_1.txt!")
#переміщуємо покажчик на початок файлу
first_file.seek(0)
#створюємо список з усіх слів у файлі
first_file_list_of_words = re.split('[ ,?\n]',first_file.read())
first_file.close()
print("File", first_file_name,"was closed!")
max_len = len(max(first_file_list_of_words,key=len))


second_file = open_file(second_file_name, "w+")
#Якщо у файлі вжу щось є - очищуємо файл
if second_file != 0:
    second_file.truncate()
# якщо довжина слова зі списку дорівнює найбільшій довжині слова
# а також якщо слово містить букву "а"
# записуємо його у другий файл
print("\nWords, that contain 'a' and have max length:")
for word in first_file_list_of_words:
    if len(word)==max_len and 'a' in word:
        second_file.write(word+"\n")
#переміщуємо покажчик на початок файлу
second_file.seek(0)
#виводимо вміст другого файлу на екран
for word in second_file.read().split('\n'):
    print(word)
second_file.close()
print("File", second_file_name,"was closed!")