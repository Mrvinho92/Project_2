user_email = {"email": "marek.parek@gmail.com"}

user_1 = dict()

user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'

user_1.update(user_email)

print("User #01:", user_1)



jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

if uzivatel.get(jmeno) == heslo:
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")



cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)

sjednocene_hodnoty = set(cisla_1) | set(cisla_2)
print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)



cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

rozdil_cisel = cisla_1.difference(cisla_2)
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)
