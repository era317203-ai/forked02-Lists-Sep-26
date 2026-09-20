# Дан список чисел. Найти сумму чисел между максимальным и минимальным числом в списке. Если максимальных/минимальных значений несколько - учитывать первое вхождение как старт и последнее как стоп.
# **Примеры**
#     Дано: `[4, **1**, 7, 9, 12, 5, 3, 6, **12**]`
#     Результат: `42`
#    Дано: `[9, **15**, 7, 9, 3, 8, 3, 10, **3**]`
#    Результат: `40`

scr = [9, 3, 1, 11, 7, 8, 14]
max_digit = max(scr)
min_digit = min(scr)
max_index = None
min_index = None
for index in range (len(scr)):
    if scr[index] == max_digit:
        max_index = index
    if scr[index] == min_digit:
        min_index = index 

                                        # print (max_digit, min_digit)
                                        # print (max_index, min_index)
if min_index < max_index:
    print (sum(scr[min_index+1: max_index]))
else:
    print (sum(scr[max_index+1: min_index]))

                                        # print (sum(scr[min_index + 1: max_index]))
                                        # print (sum(scr[max_index + 1: min_index]))
