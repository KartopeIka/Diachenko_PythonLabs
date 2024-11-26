import matplotlib.pyplot as plt

# Задаємо список
workers = [
    {"name":"Toph Beifong", "salary": 20000, "position": "police officer", "sex": "female"},
    {"name":"Jesus Christ", "salary": 40000, "position": "God", "sex": "male"},
    {"name":"Lady Gaga", "salary": 45000, "position": "Singer", "sex": "female"},
    {"name":"Oleh Vinnik", "salary": 10000, "position": "Singe", "sex": "male"},
    {"name":"Hatsune Miku", "salary": 45000, "position": "Instrument", "sex": "female"},
    {"name":"Pes Patron", "salary": 30000, "position": "Hero", "sex": "male"},
    {"name":"Stepan Vasiliyovich", "salary": 25000, "position": "Psychologist", "sex": "male"},
    {"name":"Remmi Rataulie", "salary": 18000, "position": "Chef", "sex": "male"},
    {"name":"Twighlight Sparkle", "salary": 50000, "position": "Princess", "sex": "female"},
    {"name":"Nightmare Moon", "salary": 55000, "position": "Ruler", "sex": "female"}
]

# Розподіл з категоріями
categories = {"<20000": 0, "20000-29999": 0, "30000-39999": 0, "40000-49999": 0, ">=50000": 0}
for worker in workers:
    salary = worker["salary"]
    if salary <20000:
        categories["<20000"] += 1
    elif salary <30000:
        categories["20000-29999"] += 1
    elif salary <40000:
        categories["30000-39999"] += 1
    elif salary <50000:
        categories["40000-49999"] += 1
    else:
        categories[">=50000"] += 1

# Дані для кругової діаграми
labels = list(categories.keys())
sizes = list(categories.values())

# Побудова кругової діаграми
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis("equal") # кругла діаграма
plt.title("Salary")
plt.show()