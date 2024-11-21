pocet_vyletov = int(input())

array_vstupov = [0] * pocet_vyletov

for i in range(pocet_vyletov):
    array_vstupov[i] = int(input())

for i in range(pocet_vyletov):
    if array_vstupov[i] % 13 == 0:
        print('ANO')
    elif array_vstupov[i] % 7 == 0:
        print('ANO')
    elif array_vstupov[i] % 5 == 0:
        print('ANO')
    elif array_vstupov[i] % 7 % 5 == 0:
        print('ANO')
    elif array_vstupov[i] % 13 % 7 == 0:
        print('ANO')
    elif array_vstupov[i] % 13 % 5 == 0:
        print('ANO')
    elif array_vstupov[i] % 13 % 7 % 5 == 0:
        print('ANO')
    else: print('NIE')