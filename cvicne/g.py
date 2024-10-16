pocet_prvkov = int(input())
arr_1 = [0]*pocet_prvkov
arr_2 = [0]*pocet_prvkov
arr_1 = input().split()
arr_2 = input().split()

for i in range(pocet_prvkov):
    arr_1[i] = int(arr_1[i])

for i in range(pocet_prvkov):
    arr_2[i] = int(arr_2[i])


arr_1.sort()
arr_2.sort()

for i in range(pocet_prvkov):
    if arr_1[i] + 1 == arr_2[i]:
        arr_1[i] = arr_1[i]+1

moznost = True
for i in range(pocet_prvkov):
    if arr_1[i] != arr_2[i]:
        moznost = False

if(moznost):
    print("Jednoduche")
else: print("Neda sa")