# Представляем файл в виде строки
file = open("additional_files/Задание 24/24.txt").read()

# Переменная для подсчета временной длины
n = 0
# Переменная для хранения максимальной длины
max_len = 0

# Перебираем файл по индексам
for i in range(1, len(file)):
    # Отрицающее уловие
    if file[i] == "P" and file[i - 1] == "P":
        n = 1
    else:
        n += 1
        max_len = max(max_len, n)

print(max_len)