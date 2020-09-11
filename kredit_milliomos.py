import random
import km_base
import km_kiiras


def main():
    km_kiiras.elsorajz()
    nev = input("Kérem a játékos nevét: ")
    while nev == "":
        print("Kérek egy rendes játékos nevet!")  
        nev = input("Kérem a játékos nevét: ")
    else:
        km_kiiras.menu(nev)
        utasit = input("Várom a parancsot: ")
        while utasit != "":
            km_base.parancsom(utasit, nev)
            utasit = input("Várom a parancsot: ")
        
        if utasit == "1":
            km_base.jatek(nev)
                   
        elif utasit == "3":
            km_base.dicsosegfal()
            utasit = input("Várom a parancsot: ")
            while utasit != "":
                km_base.parancsom(utasit, nev)
                utasit = input("Várom a parancsot: ")
            
        elif utasit == "2":
            km_kiiras.jatekszabalyok()
            utasit = input("Várom a parancsot: ")
            while utasit != "":
                km_base.parancsom(utasit, nev)
                utasit = input("Várom a parancsot: ")
            
        elif utasit == "4":
            quit()
     
main()