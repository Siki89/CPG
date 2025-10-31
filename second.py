def cislo_text(cislo):
    jednotky = ['', 'jedna', 'dva', 'tři', 'čtyři', 'pět', 'šest', 'sedm', 'osm', 'devět']
    desitky = ['', '', 'dvacet', 'třicet', 'čtyřicet', 'padesát', 'šedesát', 'sedmdesát', 'osmdesát', 'devadesát']
    vyjimky = ['nula', 'jedenáct', 'dvanáct', 'třináct', 'čtrnáct', 'patnáct', 'šestnáct', 'sedmnáct', 'osmnáct', 'devatenáct', 'deset']
    
    num = int(cislo)
    
    if num == 0:
        return vyjimky[0]
    elif num == 100:
        return "sto"
    elif 11 <= num <= 19:
        return vyjimky[num - 10]
    elif num == 10:
        return vyjimky[10]
    elif num < 10:
        return jednotky[num]
    else:
        des = num // 10
        jed = num % 10
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jed]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)