# Пишем рекурсивную функцию по заданию
def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + f(n - 1)
    else:
        return 2 * f(n - 2)


# Выводим результат
print(f(26))
