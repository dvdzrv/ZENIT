pocet = int(input())
vlacata = []
vystupy = []
for i in range(pocet):
    vlacata.append(input().replace('/',' ').split())
    for n in range(len(vlacata[i])):
        if vlacata[i][n] not in vystupy:
            vystupy.append(vlacata[i][n])
            print(vystupy[i])
    
print(len(vystupy))