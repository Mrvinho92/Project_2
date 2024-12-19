import datetime

aktualni_cas = datetime.datetime.now()

print("Ahoj na první lekci. Dneska máme", aktualni_cas.strftime("%d/%m/%Y"))

# Vyzkoušej si spustit tento zápis!
jmeno = "Marek"

if jmeno == "Marek":
 print("Ahoj, Marku!")
else:
 print("Ahoj, vsem ostatnim!")

 # Vyzkoušej si spustit tento zápis!
jmeno = "Matous"

if jmeno == "Marek":
 print("Ahoj, Marku!")
elif jmeno == "Lukas":
 print("Ahoj, Lukasi!")
else:
 print("Ahoj, vsem ostatnim!")