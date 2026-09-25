# Дан список чисел. Найти сумму чисел между максимальным и минимальным числом в списке. Если максимальных/минимальных значений несколько - учитывать первое вхождение как старт и последнее как стоп.
# **Примеры**
#     Дано: `[4, **1**, 7, 9, 12, 5, 3, 6, **12**]`
#     Результат: `42`
#    Дано: `[9, **15**, 7, 9, 3, 8, 3, 10, **3**]`
#    Результат: `40`

# scr = [9, 15, 7, 15, 9, 3, 8, 3, 10, 3]
# max_digit = max(scr)
# min_digit = min(scr)
# max_index = None
# min_index = None

# for index in range (len(scr)):
#     if scr[index] == max_digit:
#         max_index = index
#     if scr[index] == min_digit:
#         min_index = index 
        
#                                         # print (max_digit, min_digit)
#                                         # print (max_index, min_index)
# if min_index < max_index:
#     print (sum(scr[min_index+1: max_index]))
# else:
#     print (sum(scr[max_index+1: min_index]))

#                                         # print (sum(scr[min_index + 1: max_index]))
#                                         # print (sum(scr[max_index + 1: min_index]))



# scr = [9, 15, 7, 15, 9, 3, 8, 3, 10, 3]

# max_digit = max(scr)
# min_digit = min(scr)
# max_index = None
# min_index = None
# first_max_index = None
# first_min_index = None

# for index in range(len(scr)):
#     if scr[index] == max_digit:
#       if max_index is None and min_index is None:    # проверка на наличие записи индекса маскимального и минимального числа, если таких записей нет то это первая нужное число в последовательности.
#         max_index = index
#         first_max_index = index
#       else:
#         max_index = index
      
#     if scr[index] == min_digit:
#       if max_index is None and min_index is None:
#         min_index = index
#         first_min_index = index
#       else: 
#          min_index = index

#                                                                     # print(first_min_index)
#                                                                     # print(first_max_index)
#                                                                     # print(min_index)

# if first_min_index is not None:
#     print(sum(scr[first_min_index + 1: max_index]))
# else:
#     print(sum(scr[first_max_index + 1: min_index]))




scr = [9, 15, 15, 7, 9, 3, 8, 3, 10, 3]

max_digit = max(scr)
min_digit = min(scr)
max_index = None
min_index = None
first_max_index = None
first_min_index = None

for index in range(len(scr)):
    if scr[index] == max_digit:
      if first_max_index is None:
        first_max_index = index
      else:
        max_index = index  
    if scr[index] == min_digit:
      if first_min_index is None:
        first_min_index = index
      else:
        min_index = index

if first_min_index < first_max_index:
    print(sum(scr[first_min_index + 1: max_index]))
else:
    print(sum(scr[first_max_index + 1: min_index]))