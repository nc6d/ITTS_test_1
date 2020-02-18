"""Вводяться два цілих числа A і В. Обчислити та вивести середнє арифметичне всіх чисел з відрізка [A; B], які можна поділити
      на 3 без остачі. (0 ≤ A, B ≤ 10000)"""

diapazon = range(0, 10000)
A = int(input('Start of diapazon'))
B = int(input('End of diapazon'))
k = []
sum = 0
if not 0<=A<= 10000 or not 0<=B <= 10000:
    print("Invalid range")
else:
    for  i in range(A, B):
        if i % 3 == 0:
            k.append(i)
    print(k)
    for i in range(len(k)):
        for x in k:
            sum += x
    print(sum//len(k))