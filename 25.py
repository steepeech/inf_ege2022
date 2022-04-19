# Перебираем числа
for i in range(700001, 710000):
    # Перебериаем и собираем делители числа
    divs = []
    for d in range(2, i-1):
        if i % d == 0:
            divs.append(d)
    # Проверяем оканчиваеьтся ли сумма на 8
    if len(divs) > 0:
        if str(max(divs)+min(divs))[-1:] == "8":
            print(i, max(divs)+min(divs))

# Первые 5 строк в консоли - наш ответ