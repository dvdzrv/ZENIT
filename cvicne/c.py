n_cisel = int(input())
array_cisel = input().split()

for i in range(n_cisel):
    cislo = 0
    for n in range(n_cisel):
        if not i == n:
            cislo = cislo + int(array_cisel[n])
    print(cislo)