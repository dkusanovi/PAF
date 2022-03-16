import matplotlib.pyplot as plt
import numpy as np 


def koordinate(x1, y1, x2, y2):

	global k
	global l

	k = (y2-y1)/(x2-x1)
	l = -k*x1 + y1

	return k, l

koordinate(7, 5, 4, 3)

# Data for plotting
x = np.arange(-10, 10 , 0.01)
y = k*x + l

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x1, y1, "bo")
ax.plot(x2, y2, "bo")

ax.set(xlabel='x', ylabel='y', title='Jednadžba pravca')
ax.grid()

def izbor():

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
	

izbor()