pocet = int(input())
osemsmerovka = ['']*(2*pocet)


for i in range(pocet):
    osemsmerovka[i] = input()

for i in range(pocet):
    for n in range(pocet-4):
        riadok = str(osemsmerovka[i][n] + osemsmerovka[i][n+1] + osemsmerovka[i][n+2] + osemsmerovka[i][n+3] + osemsmerovka[i][n+4])
        if riadok  == 'ZENIT' or riadok[::-1] == 'ZENIT':
            print('jj')

for n in range(pocet):
    for i in range(pocet-4):
        stlpec = osemsmerovka[i][n] + osemsmerovka[i+1][n] + osemsmerovka[i+2][n] + osemsmerovka[i+3][n] + osemsmerovka[i+4][n]
        if stlpec == 'ZENIT' or stlpec[::-1] == 'ZENIT':
            print('jj')

for i in range(pocet-4):
    for n in range(pocet-4):
        diagonalka = osemsmerovka[i][n] + osemsmerovka[i+1][n+1] + osemsmerovka[i+2][n+2] + osemsmerovka[i+3][n+3] + osemsmerovka[i+4][n+4]
        if diagonalka == 'ZENIT' or diagonalka[::-1] == 'ZENIT':
            print('JJ')