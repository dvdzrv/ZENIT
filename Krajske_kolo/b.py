pocet = int(input())


cislo_v_bin = str(bin(pocet))[2::]

if len(cislo_v_bin) %2 != 0:
    cislo_v_bin = cislo_v_bin.zfill(len(cislo_v_bin)+1)

prehodene = [''] * len(cislo_v_bin)

for i in range(0,len(cislo_v_bin),2):
    parne = cislo_v_bin[i]
    neparne = cislo_v_bin[i+1]

    prehodene[i] = neparne
    prehodene[i+1] = parne

print(int(''.join(prehodene),2))
