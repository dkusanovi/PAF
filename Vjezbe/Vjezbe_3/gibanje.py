import particle as prt
import numpy as np
import matplotlib.pyplot as plt


p1 = prt.Particle()

p1.set_initial_conditions(10, 40, 0, 0)
# korisnik postavlja pocetne vrijednosti brzine, kuta otklona i koordinata pocetnog polozaja

#p1.reset()
# brise sve informacije o cestici

# __move()
# pomice cesticu za korak ∆t

#p1.range(0.01)
# numericki racuna domet projektila

# print(p1.plot_trajectory())
# crta putanju u x − y ravnini za trenutno stanje cestice

#p1.printInfo()


reach_a = p1.analitical()
reach_n = p1.range(0.01)

odstupanje = ((abs(reach_a - reach_n))/reach_a)*0.01
print(odstupanje)

