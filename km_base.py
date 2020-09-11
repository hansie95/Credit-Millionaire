import km_kerdes_kezeles
import km_kiiras

def jatek(nev):
    """A játék magja, ahol több függvény haszálata figyelhető meg. Jó és rossz válasz esetén elágazik a függvény. Vissza tudunk
menni a menübe, vagy akár be is fejezhetjük a játékunkat"""
    i = 1
    while i <= 15:
        nyeremenyem = km_kiiras.nyeremeny()
        lista = km_kerdes_kezeles.adatbazis()
        uj_lista = km_kerdes_kezeles.kerdes_ad(i, lista)
        helyes = uj_lista[6]
        print("\n")
        print( "{}.kérdés\t\t Eddigi nyeremény: {} kredit".format(i, nyeremenyem[i-1]))
        km_kerdes_kezeles.kerdes_kerdez(uj_lista)
        valasz = str(input("Válasz: "))
            
        while km_kerdes_kezeles.karakterhelyes_e(valasz) is not True:
            print("Kérem az 'A', 'B', 'C', 'D' választási lehetőség közül válasszon!")
            valasz = str(input("Válasz: "))
                
        ellenoriz = km_kerdes_kezeles.valasz_ellenoriz(valasz, helyes)
        if ellenoriz is True:
            print("Helyes válasz")
            print()
            i += 1
            if i == 16:
                if ellenoriz is True:
                    km_kiiras.megnyert()
                    print()
                    mentes(nev)
                    valasz_kozben = input("Szeretnél új játékot? igen/nem: ")
                    ujjatek(valasz_kozben, nev)                    
        else:
            print("ROSSZ VÁLASZ", "\t\t\t Helyes: {}".format(helyes))
            valasz_kozben = input("Szeretnél új játékot? igen(i)/nem(n): ")
            while valasz == "i" or "igen" or "n" or "nem":
                ujjatek(valasz_kozben, nev)
                valasz_kozben = input("Szeretnél új játékot? igen(i)/nem(n): ")
                
            

def ujjatek(valasz, nev):
    """Amennyiben szeretnén, elhibázott válasznál, vagy a játék megnyerése után újból kezdhetjük a játékot"""
    if valasz == "igen" or valasz == "i":
        return parancsom("1", nev)
    elif valasz == "nem" or valasz == "n":
        return quit()

        


def dicsosegfal():
    """A menüből elérhető dicsőségfal ami fájlból olvassa be azoknak az embereknek a nevét, akik hibátlanul válaszoltak
mind a 15 kérdésre"""
    print()
    print("\t\t    DICSŐSÉGFAL")
    print("\t\t    ------------\n")
    with open("dicsosegtabla.txt", "rt", encoding="UTF-8") as fajl:
        sor = fajl.readlines()
        for i in range(0, len(sor)):
            print("\t\t    " + sor[i])

def mentes(nev):
    """A mentésért felelős függvény, melyen a a játékos nevét kapjuk bemenetül és ezt fűzzük hozzá egy .txt fájlhoz"""
    with open("dicsosegtabla.txt", "at", encoding="UTF-8") as fajl:
        fajl.write(nev + "\n")


def parancsom(ertek, nev):
    """Ez a függvény az utasításokért felel amit a menüben adhatunk meg"""
    if ertek == "1":
        return jatek(nev)
    elif ertek == "2":
        return km_kiiras.jatekszabalyok()
    elif ertek == "3":
        return dicsosegfal()
    elif ertek == "4":
        return quit()