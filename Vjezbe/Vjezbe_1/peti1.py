import matplotlib.pyplot as plt
import numpy as np

x1 = float(input("x os: "))
y1 = float(input("y os: "))
x2 = float(input("x os: "))
y2 = float(input("y os: "))


def koordinate():

    k = (y2-y1)/(x2-x1)
    l = -k*x1 -y1

    if l < 0:
        print("y = " , k, "x " , l)
    else:
        print("y = " , k, "x +" , l)

    a = input("Prikazati ili spemiti? ")

    prikazati = True
    spremiti = False
    
    if prikazati: 
        plt.figure()
        plt.plot(koordinate())
        plt.show()
    else:
        plt.figure()
        plt.savefig()

    return k, l

koordinate()


