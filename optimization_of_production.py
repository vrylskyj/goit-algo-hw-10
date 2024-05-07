from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізуємо модель
model = LpProblem(name="production_optimization", sense=LpMaximize)

# Оголошуємо змінні рішення
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Обмеження на кількість використаних інгредієнтів
water_used = 2 * lemonade + fruit_juice <= 100
sugar_used = lemonade <= 50
lemon_juice_used = lemonade <= 30
fruit_puree_used = 2 * fruit_juice <= 40

# Додаємо обмеження до моделі
model += water_used, "Water"
model += sugar_used, "Sugar"
model += lemon_juice_used, "Lemon Juice"
model += fruit_puree_used, "Fruit Puree"

# Визначаємо цільову функцію
model += lemonade + fruit_juice, "Total Production"

# Розв'язуємо задачу
model.solve()

# Отримуємо результати
lemonade_production = lemonade.varValue
fruit_juice_production = fruit_juice.varValue
total_production = lemonade_production + fruit_juice_production

# Виводимо результати
print("Production Results:")
print(f"Lemonade: {lemonade_production} units")
print(f"Fruit Juice: {fruit_juice_production} units")
print(f"Total Production: {total_production} units")
