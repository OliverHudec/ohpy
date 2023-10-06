cislo = int(input(" Zadej libovolné číslo: "))
if cislo == 0:
    print(f" Číslo je nula! ")

elif cislo % 2 == 0:
    print(f" Číslo {cislo} je sudé! ")
else:
    print(f" Číslo {cislo} je liché! ")
