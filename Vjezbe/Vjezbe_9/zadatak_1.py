import bungee as b
import matplotlib.pyplot as plt


# bez otpora zraka
b1 = b.BungeeJumping(120, 50, 80, 0.01, 1, 0, 1, 45)
                     # h0, k, m, dt, rho, Cd, A, l0
b1.set_initial_conditions(120, 50, 80, 0.01, 0, 1, 1, 45)
b1.prijeposlije(0.01)
t1, y1, Euk1, Ep1, Ek1, Eel1 = b1.range_bez(0.01, 50)

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

axes[0].plot(t1, Euk1)
axes[0].plot(t1, Eel1)
axes[0].plot(t1, Ep1)
axes[0].plot(t1, Ek1)
axes[0].set_title("Ocuvanje energije")
axes[0].set_ylabel("E [J]")
axes[0].set_xlabel("t [s]")

axes[1].plot(t1, y1)
axes[1].set_title("y-t graf")
axes[1].set_ylabel("y [m]")
axes[1].set_xlabel("t [s]")

axes[0].legend(["Euk", "Eel", "Ep", "Ek"])
plt.show()



# s otporm zraka
b2 = b.BungeeJumping(120, 50, 80, 0.01, 1, 1, 1, 45)
b2.set_initial_conditions(120, 50, 80, 0.01, 1, 1, 1, 45)
b2.prijeposlije(0.01)
t2, y2, Euk2, Ep2, Ek2, Eel2 = b2.range(0.01, 50)


fig, axes = plt.subplots(1, 2, figsize=(13, 4))

axes[0].plot(t2, Euk2)
axes[0].plot(t2, Eel2)
axes[0].plot(t2, Ep2)
axes[0].plot(t2, Ek2)
axes[0].set_title("Ocuvanje energije")
axes[0].set_ylabel("E [J]")
axes[0].set_xlabel("t [s]")

axes[1].plot(t2, y2)
axes[1].set_title("y-t graf")
axes[1].set_ylabel("y [m]")
axes[1].set_xlabel("t [s]")

axes[0].legend(["Euk", "Eel", "Ep", "Ek"])
plt.show()