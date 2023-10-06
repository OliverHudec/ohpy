vyska = float(input( "Zadej tvou výšku v m: "))
hmotnost = float(input ( "Zadej tvou hmotnost: "))
bmi = hmotnost / (vyska ** 2)

print(f" Tvoje bmi je: {bmi}")

if bmi < 18.5:
    print(" Máš podváhu! ")
elif 18.5 <= bmi < 24.9:
    print(" Máš normální váhu!")
elif 24.9 > bmi < 30:
    print( "Máš nadváhu!")
else:
    print (" Máš obeziu!")
