# Змінна що зберігає назву
shop_name = "BEST DELIVERY AND SHOP PIZZA 228 BEST 1337"
# Пустий список
client_topings = []

# Виводить назву магазину в термінал
print(shop_name)

# Отримуємо данні від користувача і зберігаємо в client_order
client_order = input("Доброго дня! Який розмір піцци ви хочете замовити? \n")
print(f"Ви обрали {client_order} піццу.")

print()
print('Оберіть 5 наповнювачів. Зайві позначте знаком "-".')

# Цикл, виконує вкладені рядки визначену(5) кількість разів
for _ in range(5):
    toping = input("Оберіть наповнювач: ")
    # Додає елемент до списку
    client_topings.append(toping)

topings_list = "Ви вибрали наступні наповнювачі: \n"
for toping in client_topings:
    topings_list += toping + ", "

print(topings_list)

print("Ви вибрали наступні наповнювачі:")
for toping in client_topings:
    print(toping)