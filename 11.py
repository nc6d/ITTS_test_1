while True:
    a = int(input('Введіть A: '))
    if (a < 0) or (a > 1000000):
        print('Не в діапазоні')
    else:
        a = str(a)
        sum = 0
        for x in range(a):
            sum+=int(x)
        print(f'Сума: {sum}')
