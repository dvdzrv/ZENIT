pocet = int(input())

fotky = str(input()).rsplit()

counter = 0
last_was_0 = False


for i in range(pocet):
    if fotky[i] == '1':
        counter += 1
        last_was_0 = False
    if fotky[i] == '0' and not last_was_0:
        counter += 1
        last_was_0 = True

print(counter)