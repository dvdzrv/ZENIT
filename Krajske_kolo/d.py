pocet = int(input())
cisla = [0] * pocet
for i in range(pocet):
    cisla[i] = int(input())


def premen(cislo):
    output = []

    if cislo == 0:
        print(0)

    while cislo != 0:
        modulo = cislo % 3
        if modulo == 0:
            output.append('0')
        elif modulo == 1:
            output.append('+')
            cislo -= 1
        elif modulo == 2:
            output.append('-')
            cislo += 1
        cislo = cislo //3
    return output

for i in range(pocet):
    output = premen(cisla[i])
    output.reverse()
    print(''.join(output))