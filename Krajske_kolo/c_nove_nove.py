pocet = int(input())

fotky = input().rsplit()
print(fotky)
counter = 0

for i in range(pocet):
    if fotky[i] == '1':
        counter += 2

for i in range(1,pocet-1):
    if fotky[i-1] 



print(counter)