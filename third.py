import time
import math

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.
    """
    cislo = int(cislo)
    
    # Zpracovani hranicnich pripadu
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:  # Suda cisla vetsi nez 2 nejsou prvocisla
        return False
    
    # Testujeme delitele pouze do odmocniny cisla
    i = 0
    max_delitel = math.isqrt(cislo) + 1  # odmocnina zaokrouhlena nahoru
    for delitel in range(3, max_delitel, 2):  # testujeme pouze licha cisla
        time.sleep(0.001)
        if cislo % delitel == 0:
            print(f'Iterace {i}')
            return False
        i += 1
    
    print(f'Iterace: {i}')
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    # 999983
    print(je_prvocislo(cislo))
    # prvocisla = vrat_prvocisla(cislo)
    # print(prvocisla)