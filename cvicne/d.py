n_cisel = int(input())
array_cisel = [0]*n_cisel
vysledny_array = [0]*n_cisel

for i in range(n_cisel):
    array_cisel[i] = int(input())

for i in range(n_cisel):
    vysledny_array[i] = int((''.join((bin(array_cisel[i])[2:]).zfill(32)))[::-1], 2)
    print(vysledny_array[i])








"""
c1 = bin(1)[2:]
c1 = c1.zfill(32)
c2 = [0]*32
for i in range(len(c1)):
    c2[i] = c1[31-i]

c2 = ''.join(c2)
print(int(c2, 2))"""