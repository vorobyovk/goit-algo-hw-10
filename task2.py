import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та меж інтегрування
def f(x):
    return x**2

a = 0  # Нижня межа
b = 2  # Верхня межа

# --- 1. Обчислення інтеграла методом Монте-Карло ---
# Кількість випадкових точок
N = 100000
# Знаходимо максимальне значення функції на інтервалі [a, b]
# Оскільки f(x) = x^2 зростає на [0, 2], максимум буде в точці b
f_max = f(b)
# Генеруємо випадкові точки (x, y) в межах прямокутника,
# що обмежує область інтегрування
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f_max, N)
# Рахуємо кількість точок, що потрапили під криву y = f(x)
points_under_curve = np.sum(y_rand < f(x_rand))
# Площа прямокутника, в якому генерувалися точки
rectangle_area = (b - a) * f_max
# Оцінка площі під кривою (значення інтеграла)
monte_carlo_integral = rectangle_area * (points_under_curve / N)

# --- 2. Аналітичний розрахунок за допомогою scipy.integrate.quad ---
# Функція quad повертає результат інтегрування та оцінку похибки
analytical_integral, error = quad(f, a, b)
# --- Виведення результатів та графіку ---
# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x^2')
# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Площа інтегрування')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.legend()
plt.show()

# Виведення результатів обчислень
print("--- Результати обчислення інтеграла ---")
print(f"Значення, обчислене методом Монте-Карло: {monte_carlo_integral:.6f}")
print(f"Аналітичне значення (за допомогою quad): {analytical_integral:.6f}")
print(f"Абсолютна різниця: {abs(monte_carlo_integral - analytical_integral):.6f}")