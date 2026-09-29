# Змінна що зберігає назву
shop_name = "BEST DELIVERY AND SHOP PIZZA 228 BEST 1337"

available_topings = {
    "кетчуп": [132, 10],  # "Ключ":[Кількість в нявності, ціна]
    "курка": [132, 15],
    "сир": [87, 12],
    "Ковбаса": [144, 12],
    "Майонез": [121, 10],
    "Ананас": [111, 14],
    "Маринована_Цибуля": [156, 8],
    "Гриби": [138, 13]
    }

# Пустий список
client_topings = []

# Виводить назву магазину в термінал
print(shop_name)

# Отримуємо данні від користувача і зберігаємо в client_order
client_order = input("Доброго дня! Який розмір піцци ви хочете замовити? \n")
print(f"Ви обрали {client_order} піццу.")
print()

print("Наповнювювачі в наявності:")
for key, value in available_topings.items():
    print(f"{key.title()} в наявності.")
    print(f"Ціна: {value[1]} грн")
    print("-----")

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