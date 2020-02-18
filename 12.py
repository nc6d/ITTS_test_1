a = list()
b = list()
a = list(map(int, input("Введiть рядок N1 через пробiл:").split()))
b = list(map(int, input("Введiть рядок 21 через пробiл:").split()))
while not (0 <= len(a) <= 100) or not (0 <= len(b) <= 100):
    print("Помилка введення данних")
    a = list(map(int, input("Введiть рядок N1 через пробiл:").split()))
    b = list(map(int, input("Введiть рядок 21 через пробiл:").split()))
rez = set(set(a).symmetric_difference(set(b)))
for u in sorted(rez):
    print(u, end=' ')
