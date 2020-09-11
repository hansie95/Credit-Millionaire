def elsorajz():
    """A print függvény segítségével kirajzoltatjuk a kezdő  képernyőt"""
    return print("\n"
    "                       LEGYÉL TE IS                       \n"
    "                                                          \n"
    "            +  +  +---+  +---+  +--+   +  +---+           \n"
    "            | +   |   |  |      |   +  |    |             \n"
    "            ++    +---+  +-+    |   |  |    |             \n"
    "            | +   | +    |      |   +  |    |             \n"
    "            +  +  +  +   +---+  +--+   +    +             \n"
    "                                                          \n"
    "++   ++  +  +      +      +  +---+  ++   ++  +---+  +---+ \n"
    "| + + |  |  |      |      |  |   |  | + + |  |   |  |     \n"
    "|  +  |  |  |      |      |  |   |  |  +  |  |   |  +---+ \n"
    "|     |  |  |      |      |  |   |  |     |  |   |      | \n"
    "+     +  +  +---+  +---+  +  +---+  +     +  +---+  +---+ \n"
    "\n")


def megnyert():
    """A gratulációt kinyilvánító képernyőkép"""
    return print(""
    "--------KREDIT MILLIOMOS LETTÉL!--------\n"
    "\n"
    "                     X            X     \n"
    "   XXXXX   XXXXX    X    X   X  XXXXX   \n"
    "   X   X   X   X   X X   X   X  X   X   \n"
    "   XXXXX   XXXXX  X   X  X   X  X   X   \n"
    "   X    X  X X    XXXXX   X X   X   X   \n"
    "   XXXXXX  X  X   X   X    X    XXXXX   \n"
    "\n"
    "----A NYEREMÉNYED 50.000.000 KREDIT!----\n"
    "\n"
    "ÍGY MÁR LESZ ELÉG KREDITED A DIPLOMÁDHOZ!")


def menu(nev):
    """Bemeneten a név változó szerepel, ami az interakció miatt fontos, majd láthatjuk a menü választható elemeit"""
    return print("\n"
    "Üdvözlünk",nev +  ", a Legyél Te is Kredit Milliomos játékban!\n"
    "                                                          \n"
    "\t\t    1 - Új játék\n"
    "\t\t    2 - Játékszabályok\n"
    "\t\t    3 - Dicsőségfal\n"
    "\t\t    4 - Kilépés\n"
    "\n")

def nyeremeny():
    """Nyeremények egy listában, amit kérdésenként megjelenítünk"""
    kredit = [0,10000,20000,40000,80000,150000,300000,600000,1500000,2500000,5000000,10000000,25000000,30000000,40000000,50000000]
    return kredit


def jatekszabalyok():
    """A játékszabályokat ismertető képernyőkép"""
    return print("\n"
          "A játék szabályai roppant egyszerűek:"
          "  \n1.) 15 kérdésre kell tudjál jól válaszolni"
          "  \n2.) Amennyiben helyesen válaszolsz egy kérdésre, azt kredittel jutalmazza a játék"
          "  \n3.) Rossz válasz esetén elveszted az addig megszerzett kreditjeidet"
          "  \n4.) Amennyiben megválaszolod helyesn a 15 kérdést, felkerülsz a dicsőségfalra!\n")