

# Дан список чисел. Поменять местами первый и последний четные элементы.

scr = [1, 3, 6, 7, 5, 4, 2, 9, 2]
        # odd = [x for x in scr if x % 2 ==0]
        # print (odd)
first = None
last = None      
for index in range(len(scr)): 
    if scr[index] % 2 == 0:
        if first is None:
            first = index
        last = index
scr [first], scr [last] = scr [last], scr [first]

print (scr)
