import nltk
from matplotlib.pyplot import close
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# відкриття файлу
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        return file

# Довільний текст до 100 слів з файлу
text_file = open_file("text.txt","r")
text = text_file.read()
text_file.close()

# Токенізація по словам
tokens = word_tokenize(text)

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Функція для лемматизації
def lemmatize_word(word):
    return lemmatizer.lemmatize(word, pos='v')

# Функція для стеммінгу
def stem_word(word):
    return stemmer.stem(word)

# Лемматизація та стеммінг кожного слова
lemmatized_tokens = [lemmatize_word(word) for word in filtered_tokens]
stemmed_tokens = [stem_word(word) for word in filtered_tokens]

# Видалення пункуації
punctuation = set(string.punctuation)
cleaned_tokens = [word for word in stemmed_tokens if word not in punctuation]

# Запис обробленого тексту в новий файл
processed_text = " ".join(cleaned_tokens)

with open("processed_text.txt", "w") as file:
    file.write(processed_text)

print("Оброблений текст збережено у файлі 'processed_text.txt'.")