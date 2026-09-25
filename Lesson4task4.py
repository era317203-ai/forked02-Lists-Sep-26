# Дан список температур по дням.  
# Нужно определить **количество изменений направления**:

# - рост → падение — одно изменение;  
# - падение → рост — одно изменение.

# Подряд идущие дни с одинаковым направлением считаются одним участком.

# **Пример:**  
# `[10, 12, 14, 15, 9, 5, 3, 8, 9, 10, 9]` → `3`  
# (рост → падение → рост → падение)

scr = [10, 12, 14, 15, 15, 9, 5, 3, 8, 9, 10, 9]

directions = []
changes_count = 0
for index in range (len(scr) -1):
    if scr [index] < scr [index+1]:
        directions.append("rost") 
    elif scr [index] > scr [index+1]:
        directions.append("spad")
for index in range (len(directions) -1):
    if directions [index] != directions [index+1]:
        changes_count += 1
print (changes_count)        



temperatures = [10, 9, 12, 14, 15, 9, 5, 5, 5, 5, 3, 8, 9, 10, 9]

changes = 0
direction = 0

for i in range(len(temperatures) - 1):
    if temperatures[i + 1] > temperatures[i]:
        new_direction = 1
    elif temperatures[i + 1] < temperatures[i]:
        new_direction = -1
    else:
        new_direction = direction

    if new_direction != direction and direction != 0:
        changes += 1

    direction = new_direction

print(changes)