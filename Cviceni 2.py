zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára', 'Anežka', 'Anežka', 'Anežka']
posledni_index = len(zamestnanci) - 1
print("Na indexu 2 je:", zamestnanci[2])
print('Na', posledni_index, 'indexu je:', zamestnanci[posledni_index] )
print('V intervalu od 2 do 5 je:', zamestnanci[2:6])
print('Každý třetí člen je:', zamestnanci[::3])


jmeno = 'Martin'
vaha = 80
vyska = 2
bmi = vaha / vyska ** 2

if bmi > 40: 
    kategorie = 'tezka obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mirna nadvaha'
elif bmi > 18.5:
    kategorie = 'zdrava vaha'
else:
    kategorie = 'podvyziva'

print(jmeno, 'tve BMI je', bmi, ", coz spada do kategorie", kategorie,"." )       


zamestnanci = ['Frantisek', 'Anna', 'Jakub', 'Klara']
print("Zamestnanci na zacatku:", zamestnanci)
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anezka')
print("Nova jmena pridana:", zamestnanci_a)
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')
print("Nova jmena vlozena:", zamestnanci_b)



vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')



cislo_dne = 3

if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")

    den_tydne = tyden[cislo_dne - 1]

    if den_tydne.startswith(vstupni_pismena [cislo_dne - 1]):
        print("Spravne pismeno")

    else:
        print("Spatne pismeno!")

else:
    print("Spatna vstupni hodnota!")




