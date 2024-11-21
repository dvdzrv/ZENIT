pocet = int(input())
array_omrviniek = [''] * pocet * 2
for i in range(pocet):
    array_omrviniek[i] = str(input().split())

da_sa = True
for i in range(pocet-1):
    for n in range(pocet-1):
        if array_omrviniek[i][n] != array_omrviniek[i+1][n+1]:
            da_sa = False
            break


if da_sa:
    print('dokonale diagonalne')
else: print('kopa smetia')