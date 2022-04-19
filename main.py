




# # # № 2
# # print("x", "y", "w", "z")
# # for x in range(2):
# #     for y in range(2):
# #         for z in range(2):
# #             for w in range(2):
# #                 if not ((x or y) <= (z and w)) and (x <= w):
# #                     print(x, y, w, z)
#
# # # №5
# # n = 0
# # while True:
# #
# #     s1 = 0
# #     s2 = 0
# #
# #     # сумма четных цифр
# #     for i in str(n):
# #         if int(i) % 2 == 0:
# #             s1 += int(i)
# #
# #     # цумма цифр на четных позициях
# #     for i, x in enumerate(str(n), 1):
# #         if i % 2 == 0:
# #             s2 += int(x)
# #
# #     if s1 - s2 == 11 or s1 - s2 == -11:
# #         print(n)
# #         break
# #     n += 1
#
#
# # # №6
# # x=[]
# # for i in range(1, 1000):
# #     s = i
# #     s = 5 * (s // 7)
# #     n = 1
# #     while s < 500:
# #         s = s + 15
# #         n = n * 2
# #
# #         if n == 512:
# #             print(i)
# #             x.append(i)
# # print(len(x))
#
# # # №8
# # n = 0
# # letters = ["а", "в", "е", "и", "к", "н", "о", "р"]
# # for a1 in letters:
# #     for a2 in letters:
# #         for a3 in letters:
# #             st = a1 + a2 + a3
# #
# #             if st.count("в") == 1:
# #                 n += 1
# #                 if st.count("а") == 0:
# #                     print(n)
# #                     exit()
# #
# # print(n)
#
#
# # # №12
# #
# # x = "8"*84
# # while "1111" in x or "8888" in x:
# #     if "1111" in x:
# #
# #         x = x.replace("1111", "8", 1)
# #     else:
# #         x = x.replace("8888", "11", 1)
# #
# # print(x)
# #
#
#
#
#
# # №14
# x = 12**34+7+12**26-3*12**16+2*12**5+552
#
# k = ""
# while x > 0:
#     k = str(x % 12) + k
#     x = x // 12
#
# print(len(set(k)))
#
#
# #
# #
# # # №15
# # A = 1
# # while True:
# #     flag = True
# #     for x in range(1, 1000):
# #         for y in range(1, 1000):
# #             if not((y-x < A) or (7*x+4*y>350) or (3*y-2*x>45)):
# #                 flag = False
# #                 break
# #     if flag:
# #         print(A)
# #     A += 1
# #
# #
# # №16
#
#
# #
# # def f(n):
# #     if n == 0:
# #         return 0
# #     elif n % 2 == 0 and n > 0:
# #         return f(n / 2)
# #     elif n % 2 != 0:
# #         return f(n - 1) + 1
# #
# #
# # for i in range(0, 100000000 + 1):
# #     if f(i) == 2:
# #         k += 1
# #
# # print(k)
# # # №17
# # s = []
# # for i in range(11000, 22001):
# #     k = 0
# #     for j in [11, 13, 17, 19]:
# #         if i % j == 0:
# #             k += 1
# #     if k == 2:
# #         s.append(i)
# #
# # print(len(s), min(s))
#
#
# # №18
# # file = list(map(int, [i for i in open("17-1.txt")]))
# # sred = sum(file) // len(file)
# # x = []
# #
# # for i in range(2, len(file)):
# #     if str(file[i])[-2:] == "14" or str(file[i - 1])[-2:] == "14" or str(file[i - 2])[-2:] == "14":
# #         n = [j for j in [file[i], file[i - 1], file[i - 2]] if j < sred]
# #         if len(n) >= 2:
# #             x.append(file[i]+file[i - 1]+file[i - 2])
# #
# # print(max(x), len(x))
#
# # # №22
# # for x in range(1000, 0, -1):
# #     a = 7 * x + 27
# #     b = 7 * x - 33
# #     while a != b:
# #         if a > b:
# #             a -= b
# #         else:
# #             b -= a
# #
# #     if a == 10:
# #         print(x)
#
#
# # s = []
# #
# # for x in range(100):
# #     for y in range(100):
# #         flag = True
# #         for a in range(-100, 100):
# #
# #             if not ((2 * x + 3 * y < a) or (x > y) or (y > 24)):
# #                 flag = False
# #                 break
# #
# #         if flag:
# #             s.append(a)
# #
# # print(s)
#
#
# #
# # #
# # s = []
# # max_para = 0
# # file = list(map(int, [i for i in open("17.txt")]))
# # for i in range(1, len(file)):
# #     if (file[i-1] % 5 == 0 or file[i] % 5 == 0) and ((file[i-1]+file[i]) % 7 == 0):
# #         s.append(file[i-1]+file[i])
# # print(len(s), max(s))
#
# #
# #
# # k = 0
# # file = str(open("24.txt", "r"))
# # for i in range(3, len(file)):
# #     if file[i] + file[i - 1] != file[i - 2] + file[i - 3]:
# #         k += 1
# # print(k)
# # # # №23
# # def f1(x, y):
# #     if x > y:
# #         return 0
# #     if x == y:
# #         return 1
# #     if x < y:
# #         return f1(x + 1, y) + f1(x * 3, y)
# #
# #
# # print(f1(2, 26) * f1(26, 87))
# #
# #
# # x = []
# # x1 = []
# # for i in range(10000000, 10000000000000000):
# #     print(i)
# #     for i1 in range(i-1, 0, -1):
# #         if len(x1) < 2:
# #             if i%i1 == 0:
# #                 x1.append(i1)
# #         else:
# #             if 0<sum(x1)<10000:
# #                 x.append(sum(x1))
# #             break
# #
# #     if len(x) == 5:
# #         print(x)
#
# # file = [max(list(map(int, i))) for i in [i.split(" ") for i in open("27_A.txt")]]
# # if sum(file) % 109 != 0:
# #     print(sum(file))
#
#
# # file = [int(i) for i in open("27-B.txt")]
# # sorted_file = sorted(file, reverse=True)
# #
# # for i1 in sorted_file:
# #     for i2 in sorted_file[1:]:
# #         for i3 in sorted_file[2:]:
# #             if (i1+i2+i3) % 3 == 0:
# #                 print(i1+i2+i3)
#
# # import itertools
# #
# # s = '2' * 4 + '3' * 3 + '4' * 2
# #
# # max_sum = 0
# # for i in itertools.permutations(s):
# #     new = ''.join(i)
# #     while '42' in new or '32' in new:
# #         if '42' in new:
# #             new = new.replace('42', '51', 1)
# #         else:
# #             new = new.replace('32', '61', 1)
# #     str_sum = [int(x) for x in new]
# #     if sum(str_sum) > max_sum:
# #         max_sum = sum(str_sum)
# # print(max_sum * 5)
#
# # # 24
# # file = str(open("24.txt").read())
# # print(file.find("XYZ") + file.find("ZYX"))
#
#
# # file = open("zadanie_26.txt").readlines()
# # other_arch = []
# # y = [65536 for i in range(8)]
# #
# # for arch in file:
# #     for disk in range(8):
# #         if int(arch) <= y[disk]:
# #             y[disk] = y[disk]-int(arch)
# #             break
# #     else:
# #         other_arch.append(int(arch))
# #
# # print(sum(other_arch), len(other_arch))
#
#
# # # 5
# # for i in range(100, 1000):
# #     i = str(i)
# #     x = [i[j-2:j] for j in range(2, len(i)+1)]
# #     if max(map(int, x)) + min(map(int, x)) == 137:
# #         print(i)
#
# # # 6
# # k = 0
# # file = [list(map(int, i.split())) for i in open("9.txt").readlines()]
# # for i in file:
# #     if (i[0]+i[1]+i[2]) % 2 != 0 or (i[0]+i[1]+i[3]) % 2 != 0 or (i[0]+i[2]+i[3]) % 2 != 0 or (i[1]+i[2]+i[3]) % 2 != 0:
# #         k += 1
# # print(k)