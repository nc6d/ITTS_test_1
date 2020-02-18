a, b = int(input()), int(input())
c = []
if not 0 <= a <= 10000 or not 0 <= b <= 10000:
    print("Error")
else:
    for i in range(b, a - 1, -1):
        if i % 2 == 0:
            c.append(i)
print(c)
