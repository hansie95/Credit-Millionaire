import random

class Kerdes:
    def __init__(self,kerdes,A,B,C,D):
        self.kerdes = kerdes
        self.A = A
        self.B = B
        self.C = C
        self.D = D

def adatbazis():
    """Egy külső .txt fájlból csinál egy hasznáható listát, amiben nincsenek \n jelek és a ahol tabulátort talál,
        ott elválasztja a lista elemeit"""
    with open("adatb_szoveges_eles.txt", "rt", encoding="UTF-8") as fajl:
        sor = fajl.readlines()
        lista = []
        helyes_lista = []
        for i in range(0, len(sor)):
            lista.append(sor[i].strip("\n"))
        for x in range(0, len(lista)):
            helyes_lista.append(lista[x].split("\t"))
    return helyes_lista


def kerdes_ad(nehezseg, lista):
    """A függvény bementetül kap egy nehezsegi fokot 1-15 ig és magát a helyes listát amiből a nehezségi fokoknak
megfelelően generál egy új listát amit a progrmunk során immáron látható módon felhasználunk"""
    uj_lista = []
    for i in range(0, len(lista)): 
        if nehezseg == 1 and lista[i][0] == "1":
            uj_lista.append(lista[i])
        elif nehezseg == 2 and lista[i][0] == "2":
            uj_lista.append(lista[i])
        elif nehezseg == 3 and lista[i][0] == "3":
            uj_lista.append(lista[i])
        elif nehezseg == 4 and lista[i][0] == "4":
            uj_lista.append(lista[i])
        elif nehezseg == 5 and lista[i][0] == "5":
            uj_lista.append(lista[i])
        elif nehezseg == 6 and lista[i][0] == "6":
            uj_lista.append(lista[i])
        elif nehezseg == 7 and lista[i][0] == "7":
            uj_lista.append(lista[i])
        elif nehezseg == 8 and lista[i][0] == "8":
            uj_lista.append(lista[i])
        elif nehezseg == 9 and lista[i][0] == "9":
            uj_lista.append(lista[i])
        elif nehezseg == 10 and lista[i][0] == "10":
            uj_lista.append(lista[i])
        elif nehezseg == 11 and lista[i][0] == "11":
            uj_lista.append(lista[i])
        elif nehezseg == 12 and lista[i][0] == "12":
            uj_lista.append(lista[i])
        elif nehezseg == 13 and lista[i][0] == "13":
            uj_lista.append(lista[i])
        elif nehezseg == 14 and lista[i][0] == "14":
            uj_lista.append(lista[i])
        elif nehezseg == 15 and lista[i][0] == "15":
            uj_lista.append(lista[i])
        szam = random.randint(0, len(uj_lista))
    return uj_lista[szam-1]


def kerdes_kerdez(lista):
    """A függvénybe bementeként a hasznáható listát kapjuk és a feldarabol részeit elhelyezi. Itt a kérdést és a válaszokat
használjuk fel."""
    kerdesvalasz = Kerdes(lista[1], lista[2], lista[3], lista[4], lista[5])
    print(len(kerdesvalasz.kerdes)*"-")
    print(kerdesvalasz.kerdes)
    print(len(kerdesvalasz.kerdes)*"-")
    print("A: " + kerdesvalasz.A, "\t\t\t B: " + kerdesvalasz.B, "\n"
          "C: " + kerdesvalasz.C, "\t\t\t D: " + kerdesvalasz.D)
    print("-"*len(kerdesvalasz.kerdes))
    

def karakterhelyes_e(karakter):
    """Fontos, hogy az adott válasz helyes legyen amit a játékostól kapunk, ezért az inputon lefuttatjuk a kapott válasz
karakter és, ha nem megfelelő akkor hibát dob, ha meg helyes akkor tovább mehet."""
    valaszlehetosegek = ['a','b','c','d','A','B','C','D']
    for x in range(0, len(valaszlehetosegek)):
        if karakter == valaszlehetosegek[x]:
            return True
        
def valasz_ellenoriz(valasz, helyes):
    """ A karakter ellenörző után ez a függvény leellenőrzi, hogy a kérdésre helyes válasz jött-e? Ezt úgy csinálja, hogy
a program által használt listában, van egy helyes oszlop a kérdésekhez, és összeveti, hogy az inputon beérkező válasz
megegyezik-e a listában található helyes válasszal"""
    if valasz.upper() == helyes:
        return True
    return False


