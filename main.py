# Змінна що зберігає назву
shop_name = "BEST DELIVERY AND SHOP PIZZA 228 BEST 1337"

available_topings = {
    "кетчуп": [0, 10],  # "Ключ":[Кількість в нявності, ціна]
    "курка": [132, 15],
    "сир": [87, 12],
    "Ковбаса": [144, 12],
    "Майонез": [121, 10],
    "Ананас": [111, 14],
    "Маринована Цибуля": [156, 8],
    "Гриби": [138, 13]
    }

# Пустий список
client_topings = []

# Максимум наповнювачів у замовленні
max_topings_count = 5

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
print(f'Оберіть {max_topings_count} наповнювачів. Коли завершите, поставте "-" ')
topings_list = "Ви вибрали наступні наповнювачі: \n"
# Цикл, виконує вкладені рядки визначену кількість разів
for _ in range(max_topings_count):
    input_toping = input("Наповнювач: ")
    input_toping.title()

    for toping, num_in_storage in available_topings.items():
        toping.title()
        if input_toping == toping and num_in_storage[0] > 0:
            # Додає елемент до списку
            client_topings.append(toping)
            topings_list += toping + ", "
        elif num_in_storage <= 0:
            

print(topings_list)