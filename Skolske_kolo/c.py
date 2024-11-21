riadok1 = input()
riadok2 = input()
riadok3 = input()
riadok4 = input()
pocet_voznov = 0

for i in range(len(riadok2)):
    if riadok2[i] == 'O':
        pocet_voznov = pocet_voznov + 1

print(int(pocet_voznov/4))