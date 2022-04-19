# Сортируем строку
letters = sorted("ЛЕМУР")
# Переменная для подсчета порядкового номера строки
n = 0

# Собираем строки
for i1 in letters:
    for i2 in letters:
        for i3 in letters:
            for i4 in letters:
                # Сама строка
                x = i1 + i2 + i3 + i4
                n += 1

                # Проверяем строку
                if x[0] == "Л":
                    print(n)
                    exit()
