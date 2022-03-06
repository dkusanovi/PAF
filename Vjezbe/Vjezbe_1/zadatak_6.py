import matplotlib.pyplot as plt
import numpy as np
import math 

def kruznica(a, b, x0, y0, r): # koordinate tocke, koordinate ishodista kruznice, radijus kruznice

    udaljenost = math.sqrt((b-y0)**2+(a-x0)**2) # od ishodista
    udaljenost2 = math.sqrt((b-y0)**2+(a-x0)**2)-r # od kruznice

    if udaljenost < r:
        print("Tocka se nalazi unutar kruznice na udaljenosti", abs(udaljenost2), "od kruznice.")
    elif udaljenost == r:
        print("Tocka se nalazi na kruznici.")
    else:
        print("Tocka se nalazi izvan kruznice na udaljenosti", udaljenost2, "od kruznice.")

    kruz = plt.Circle((x0, y0), r, color = "r", fill = False)
    fig, ax = plt.subplots()
    ax.add_patch(kruz)
    ax.set_aspect("equal", adjustable = "datalim")
    ax.plot(a, b, "bo")
    ax.plot()
    
    while True:
        prikaz = input("Unesite p za prikazati ili s za spremiti? ")
        prikaz = prikaz.lower()

        if prikaz == "p":
            plt.show()
            break
        elif prikaz == "s":
            ime = input("Kako zelite nazvati sliku? ")
            plt.savefig(ime)
            break
        else:
            print("Pokusajte ponovo :) ")


kruznica(2, -6, 2, 4, 7)