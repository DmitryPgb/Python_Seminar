# Найти максимальное из пяти чисел

a = [1,9,3,4,5]
print(a)
max = 0

for i in a:
    if max < i:
        max = i

print(max)
