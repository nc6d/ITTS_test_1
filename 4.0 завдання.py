a = input('Input 0  >= n >= 100: ')
n = list(map(int,a.split()))
b = []
new_n = []
while len(n) > 100:
 print('Wrong length.')
 n = [input('Try again: ')]
for i in range(len(n)):
 if n[i] < n[i - 1]:
  x = new_n.append(n[i])
  b.append(i)
 else:
  continue
x =list(map(int, new_n))
print(b)
print(len(x))
