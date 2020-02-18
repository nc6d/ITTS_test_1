while True:
    a = int(input('Input number'))
    if 0 <= a <= 1000000:
        break
one = 0
while a != 0:
    one = a % 10
    print(one, end="")
    a = a // 10
