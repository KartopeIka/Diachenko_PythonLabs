import json

# Ініціалізація даних
workers = {
    "Toph Beifong": {"salary": 20000, "position": "police officer", "sex": "female"},
    "Jesus Christ": {"salary": 40000, "position": "God", "sex": "male"},
    "Lady Gaga": {"salary": 45000, "position": "Singer", "sex": "female"},
    "Oleh Vinnik": {"salary": 10000, "position": "Singe", "sex": "male"},
    "Hatsune Miku": {"salary": 45000, "position": "Instrument", "sex": "female"},
    "Pes Patron": {"salary": 30000, "position": "Hero", "sex": "male"},
    "Stepan Vasiliyovich": {"salary": 25000, "position": "Psychologist", "sex": "male"},
    "Remmi Rataulie": {"salary": 18000, "position": "Chef", "sex": "male"},
    "Twighlight Sparkle": {"salary": 50000, "position": "Princess", "sex": "female"},
    "Nightmare Moon": {"salary": 55000, "position": "Ruler", "sex": "female"}
}

# Запис початкових даних у файл
with open("Workers_data.json", "wt") as file:
    json.dump(workers, file, indent=4)

# Завантаження даних з JSON-файлу
def load(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return {}

# Збереження даних у JSON-файл
def save(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Виведення вмісту JSON-файлу
def display(filename):
    data = load(filename)
    if data:
        for name, details in data.items():
            print(f"Name: {name}, Salary: {details['salary']}, Position: {details['position']}, sex: {details['sex']}")
    else:
        print("File is empty or not found.")

# Додавання нового запису
def add(filename):
    data = load(filename)
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    position = input("Enter position: ")
    sex = input("Enter sex (male/female): ")

    data[name] = {"salary": salary, "position": position, "sex": sex}
    save(data, filename)
    print(f"{name} successfully added.")

# Видалення запису за ім'ям
def delete(filename):
    data = load(filename)
    name = input("Enter name to delete: ")
    if name in data:
        del data[name]
        save(data, filename)
        print(f"{name} successfully deleted.")
    else:
        print(f"{name} not found.")

# Пошук за іменем
def search(filename):
    data = load(filename)
    name = input("Enter name to search: ")
    if name in data:
        details = data[name]
        print(f"Name: {name}, Salary: {details['salary']}, Position: {details['position']}, sex: {details['sex']}")
    else:
        print(f"{name} not found.")


# Пошук людей з мінімальною та максимальною зарплатами
def min_max_salary(filename, output_filename):
    data = load(filename)
    data_keys = list(data.keys())
    min_salary_worker_name = data_keys[0]
    max_salary_worker_name = data_keys[0]
    for worker in data_keys:
        if data[worker]["salary"]<data[min_salary_worker_name]["salary"]:
            min_salary_worker_name = worker
        if data[worker]["salary"] > data[max_salary_worker_name]["salary"]:
            max_salary_worker_name = worker

    print(f"Min salary worker: {min_salary_worker_name}: {data[min_salary_worker_name]}\n"
          f"Max salary worker: {max_salary_worker_name}: {data[max_salary_worker_name]}")

    # Зберігаємо результат у файл
    with open(output_filename, "wt") as file:
        json.dump({"Min salary worker": {min_salary_worker_name:data[min_salary_worker_name]},
                   "Max salary worker": {max_salary_worker_name:data[max_salary_worker_name]}}, file, indent=4)

# Основна програма
filename = "Workers_data.json"
output_filename = "min_max_salary.json"

print("\nShow file content ->1<-\n"
      "Add worker ->2<-\n"
      "Delete worker ->3<-\n"
      "Find worker by name ->4<-\n"
      "Find min and max salary worlers ->5<-\n"
      "Exit program ->0<-")

while True:
    x = input("\nSelect action: ")
    match x:
        case "1":
            display(filename)
        case "2":
            add(filename)
        case "3":
            delete(filename)
        case "4":
            search(filename)
        case "5":
            min_max_salary(filename, output_filename)
        case "0":
            print("Program terminated.")
            break
        case _:
            print("Invalid input. Please try again.")