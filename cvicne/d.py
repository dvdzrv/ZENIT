n_cisel = int(input())
array_cisel = [0]*n_cisel
vysledny_array = [0]*n_cisel

for i in range(n_cisel):
    array_cisel[i] = int(input())

for i in range(n_cisel):
    vysledny_array[i] = int(   (  (   bin(array_cisel[i])[2:]   ).zfill(32)   )[::-1], 2)
    print(vysledny_array[i])



"""
array_cisel[i] <- výber čísla

bin(array_cisel[i]) <- premena čísla do 2kovej sústavy

bin(array_cisel[i])[2:] <- odstránenie 0b prefixu

bin(array_cisel[i])[2:].zfill(32) <- doplenenie cifier na 32 bit

(((bin(array_cisel[i])[2:]).zfill(32))[::-1] <- otočenie arrayu

int(((bin(array_cisel[i])[2:]).zfill(32))[::-1], 2) <- premena na 10tkovú sústavu

"""



"""
#PRVY POKUS LOL


c1 = bin(1)[2:]
c1 = c1.zfill(32)
c2 = [0]*32
for i in range(len(c1)):
    c2[i] = c1[31-i]

c2 = ''.join(c2)
print(int(c2, 2))"""