rozpravka = "Raz dávno v krajine kódu, v meste Algoria, žil šikovný programátor menom Alan. Alan bol obľúbený v celej Algorii pre svoje zručnosti a múdrosť v kóde. Jedného dňa, keď Alana navštívil tajomný robot s menom Robi, zistil o záhadnej úlohe, ktorá ho čakala. Robi šepkal Alanovi do ucha: “V tvojom kóde sa skrýva tajomstvo, najdlhšie slovo ti odhalí cestu. Ale choď opatrne, môže to byť ťažký úkol.” Alan sa zatváril vážne a bez váhania sa pustil do práce. Začal prechádzať kód riadok po riadku, hľadajúc tú správnu cestu. Každý riadok bol plný rôznych premenných, cyklov a podmienok. Alan sa nemohol nechať zmiasť, musel nájsť to najdlhšie slovo, čo i len jediné. Po niekoľkých hodinách pátrania Alan konečne narazil na slovo, ktoré malo nezameniteľný lesk. “Európska”, zaznelo ticho z jeho úst, keď napokon objavil to najdlhšie slovo, ktorému sa venoval celý jeho úsilný prieskum. A tak, s najdlhším slovom v jeho kóde, Alan odhalil tajomstvo, ktoré mu odhalilo nový svet možností a algoritmov. Robi s úctou naklonil hlavu a odviedol Alana do nového sveta, kde boli len možnosti a žiadne hranice. A Alan zostal zapamätaný ako hrdina, ktorý našiel to najdlhšie slovo a otvoril cestu novému veku programovania v Algorii."


diakritika = ['ľ', 'š', 'č', 'ť', 'ž', 'ý', 'á', 'í', 'é', 'ú', 'ä', 'ô', 'ň']
bez_diakritiky = ['l', 's', 'c', 't', 'z', 'y', 'a', 'i', 'e', 'u', 'a', 'o', 'n']

rozpravka = rozpravka.replace('.', '')
rozpravka = rozpravka.replace('"', '')

for i in range(len(diakritika)):    
    rozpravka = rozpravka.replace(diakritika[i], bez_diakritiky[i])

rozpravka = rozpravka.split()

pocet_znakov = 0
for i in range(len(rozpravka)):
    if len(rozpravka[i]) > pocet_znakov:
        slovo = rozpravka[i]
        pocet_znakov = len(rozpravka[i])

print(slovo, pocet_znakov)

