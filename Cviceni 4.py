veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = {'souhlasky': 0, 'samohlasky': 0}

for pismeno in veta:
    if not pismeno.isalpha():
        continue
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    elif pismeno.lower() in souhlasky:
        vysledek['souhlasky'] += 1

print('Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky'])





cisla = [1, 2, 3, 4, 5, 6, 7, 8]
licha = 0
suda = 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo

vysledek = abs(suda - licha)
print('Rozdíl je:', vysledek)








vysledek = list()
start = 3
stop = 9
delitel = 3


vysledek = []
start = 3
stop = 9
delitel = 3

if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    for number in range(start, stop + 1):
        if number % int(delitel) == 0:
            vysledek.append(number)
    print('Čísla dělitelná', delitel, ':', vysledek)
else:
    print('Zadané vstupy musí být čísla.')

    






seznam_slov = ['jablko', 'pomeranč', 'banán', 'kiwi', 'hruška']
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delky_slov)

