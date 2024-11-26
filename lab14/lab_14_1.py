import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,10,100) # діапазон значень для х
y=(1/x)*np.cos(x**2+1/x) # визначення функції у(х)

plt.plot(x, y, label='(1/x)*cos(x^2+1/x)', color = "purple", linewidth = 4) # побудова графіка

plt.title('Function graph', fontsize=15)   # назва графіка
plt.xlabel('x', fontsize=15, color='blue') # позначення вісі абсцис
plt.ylabel('y', fontsize=15, color='blue') # позначення вісі ординат
plt.legend() # додавання легенди
plt.grid(True) # додавання сітки
plt.show() # відображення графіка