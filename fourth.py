def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Ověření, zda cílová pozice není mimo šachovnici
    radek_cil, sloupec_cil = cilova_pozice
    if radek_cil < 1 or radek_cil > 8 or sloupec_cil < 1 or sloupec_cil > 8:
        return False
    
    # Ověření, zda cílová pozice není obsazená
    if cilova_pozice in obsazene_pozice:
        return False
    
    typ_figurky = figurka["typ"]
    aktualni_pozice = figurka["pozice"]
    radek_akt, sloupec_akt = aktualni_pozice
    
    # Pokud se figurka nepohne, není to platný tah
    if aktualni_pozice == cilova_pozice:
        return False
    
    # Pravidla pro jednotlivé figury
    if typ_figurky == "pěšec":
        return _je_tah_mozny_pesec(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "jezdec":
        return _je_tah_mozny_jezdec(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "věž":
        return _je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "střelec":
        return _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "dáma":
        return _je_tah_mozny_dama(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "král":
        return _je_tah_mozny_kral(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    return False


def _je_tah_mozny_pesec(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb pěšce"""
    radek_akt, sloupec_akt = aktualni_pozice
    radek_cil, sloupec_cil = cilova_pozice
    
    # Pěšec se pohybuje pouze dopředu (zvyšuje řádek)
    if sloupec_cil != sloupec_akt:  # Pěšec se nemůže pohybovat do strany
        return False
    
    # Ověření pohybu o 1 pole dopředu
    if radek_cil == radek_akt + 1 and cilova_pozice not in obsazene_pozice:
        return True
    
    # Ověření pohybu o 2 pole dopředu z výchozí pozice
    if radek_akt == 2 and radek_cil == radek_akt + 2:
        # Kontrola, zda pole mezi výchozí a cílovou pozicí není obsazené
        mezilehla_pozice = (radek_akt + 1, sloupec_akt)
        if mezilehla_pozice not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
            return True
    
    return False


def _je_tah_mozny_jezdec(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb jezdce"""
    radek_akt, sloupec_akt = aktualni_pozice
    radek_cil, sloupec_cil = cilova_pozice
    
    # Jezdec se pohybuje ve tvaru L: (2,1) nebo (1,2)
    radek_diff = abs(radek_cil - radek_akt)
    sloupec_diff = abs(sloupec_cil - sloupec_akt)
    
    return (radek_diff == 2 and sloupec_diff == 1) or (radek_diff == 1 and sloupec_diff == 2)


def _je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb věže"""
    radek_akt, sloupec_akt = aktualni_pozice
    radek_cil, sloupec_cil = cilova_pozice
    
    # Věž se pohybuje pouze horizontálně nebo vertikálně
    if radek_akt != radek_cil and sloupec_akt != sloupec_cil:
        return False
    
    return _je_cesta_volna(aktualni_pozice, cilova_pozice, obsazene_pozice)


def _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb střelce"""
    radek_akt, sloupec_akt = aktualni_pozice
    radek_cil, sloupec_cil = cilova_pozice
    
    # Střelec se pohybuje pouze diagonálně
    if abs(radek_cil - radek_akt) != abs(sloupec_cil - sloupec_akt):
        return False
    
    return _je_cesta_volna(aktualni_pozice, cilova_pozice, obsazene_pozice)


def _je_tah_mozny_dama(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb dámy"""
    # Dáma kombinuje pohyb věže a střelce
    return (_je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice) or 
            _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice))


def _je_tah_mozny_kral(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """Ověří pohyb krále"""
    radek_akt, sloupec_akt = aktualni_pozice
    radek_cil, sloupec_cil = cilova_pozice
    
    # Král se pohybuje o 1 pole v libovolném směru
    radek_diff = abs(radek_cil - radek_akt)
    sloupec_diff = abs(sloupec_cil - sloupec_akt)
    
    return radek_diff <= 1 and sloupec_diff <= 1 and (radek_diff != 0 or sloupec_diff != 0)


def _je_cesta_volna(odkud, kam, obsazene_pozice):
    """Ověří, zda je cesta mezi dvěma pozicemi volná (pro věž, střelce, dámu)"""
    radek_od, sloupec_od = odkud
    radek_kam, sloupec_kam = kam
    
    # Určení směru pohybu
    krok_radek = 0 if radek_kam == radek_od else (1 if radek_kam > radek_od else -1)
    krok_sloupec = 0 if sloupec_kam == sloupec_od else (1 if sloupec_kam > sloupec_od else -1)
    
    # Kontrola všech polí mezi výchozí a cílovou pozicí (bez cílové)
    aktualni_radek = radek_od + krok_radek
    aktualni_sloupec = sloupec_od + krok_sloupec
    
    while (aktualni_radek != radek_kam or aktualni_sloupec != sloupec_kam):
        if (aktualni_radek, aktualni_sloupec) in obsazene_pozice:
            return False
        
        aktualni_radek += krok_radek
        aktualni_sloupec += krok_sloupec
    
    return True


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True