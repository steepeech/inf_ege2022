# Представляем файл в виде списка цифр
file = open("additional_files/Задание 17/17.txt").readlines()
file = [int(i) for i in file]

# Переменная для хранения сумм пар
s = []
for i in range(1, len(file)):
    # Проверяем пару по условию
    if file[i] % 3 == 0 or file[i - 1] % 3 == 0:
        # Добавляем если подходит
        s.append(file[i] + file[i - 1])

print(len(s), max(s))