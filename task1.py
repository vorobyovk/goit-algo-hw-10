import pulp

# Створюємо об'єкт задачі лінійного програмування, вказуючи, що ми хочемо максимізувати цільову функцію
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Визначаємо змінні для кількості кожного продукту.
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Ціль - максимізувати загальну кількість вироблених напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Відображення створеної моделі (необов'язково, але корисно для перевірки)
print("Модель лінійного програмування:")
print(model)

model.solve()

#Виведення результатів
print("\n" + "="*30)
print(f"Статус вирішення: {pulp.LpStatus[model.status]}")
print("="*30)
print("\nОптимальний план виробництва:")
print(f"Кількість 'Лимонаду' до виробництва: {int(pulp.value(lemonade))}")
print(f"Кількість 'Фруктового соку' до виробництва: {int(pulp.value(fruit_juice))}")
print(f"\nЗагальна максимальна кількість вироблених продуктів: {int(pulp.value(model.objective))}")
print("\nВикористання ресурсів:")
water_used = 2 * pulp.value(lemonade) + 1 * pulp.value(fruit_juice)
sugar_used = pulp.value(lemonade)
lemon_juice_used = pulp.value(lemonade)
fruit_puree_used = 2 * pulp.value(fruit_juice)

print(f"Вода: {water_used} / 100 од.")
print(f"Цукор: {sugar_used} / 50 од.")
print(f"Лимонний сік: {lemon_juice_used} / 30 од.")
print(f"Фруктове пюре: {fruit_puree_used} / 40 од.")