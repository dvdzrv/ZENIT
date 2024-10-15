n_cisel = int(input())
array_cisel = [0]*n_cisel
vysledny_array = [0]*n_cisel

for i in range(n_cisel):
    array_cisel[i] = int(input())

for i in range(n_cisel):
    vysledny_array[i] = int(   (  (   bin(array_cisel[i])[2:]   ).zfill(32)   )[::-1], 2)
    print(vysledny_array[i])