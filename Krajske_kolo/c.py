pocet = int(input())

fotky = input().rsplit()
fotky.append('E')

otvorena_Fotka = False
counter = 0

for i in range(pocet):
    if fotky[i] == '1':
        if fotky[i+1] == '1':
            counter += 1
        else: counter += 2
        if i != len(fotky) and fotky[i+1] == 'E':
            counter += 1

print(counter-1)