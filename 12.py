# 70 идущих подряд цифр 8
s = "8" * 70

# Просто преписываем программу
while "2222" in s or "8888" in s:
    if "2222" in s:
        s = s.replace("2222", "88", 1)
    else:
        s = s.replace("8888", "22", 1)

print(s)