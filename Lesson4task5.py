# Проверить **симметрична** ли квадратная матрица относительно **побочной диагонали**.
# Дан список списков размера N × N. 
# Побочная диагональ — это диагональ, проходящая от **верхнего правого угла к нижнему левому**.
# Вывести YES, если симметрична, иначе NO.

# **Пример**
# - Дано
# `[
#     [1, 2, 3],
#     [4, 5, 2],
#     [3, 4, 1]
# ]`
# Результат: YES

# - Дано:
# `[
#     [7, 8, 9],
#     [1, 5, 3],
#     [9, 2, 7]
# ]`
# Результат: NO


src =[
     [1, 2, 3],
     [4, 5, 2],
     [3, 4, 1]
     ]

lenght = len(src) 
simmetric = True
for x in range (lenght):
    for y in range (lenght):
        if src [x] [y] != src [lenght - 1 - y] [lenght - 1 - x]:
            simmetric = False

if simmetric is True: 
    print ("YES")

else:
    print ("NO")

print (simmetric)
                #print (src [0] [0])
                #print (src[0])

