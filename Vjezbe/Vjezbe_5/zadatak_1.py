import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import math


ho1 = ho.HarmonicOscillator(5, 0, 10, 15, 0.1)

ho1.set_initial_conditions(5, 0, 10, 15, 0.1, 0.1)
#ho1.graf()


ho2 = ho.HarmonicOscillator(5, 0, 10, 15, 0.05)

ho2.set_initial_conditions(5, 0, 10, 15, 0.1, 0.05)
#ho2.graf()

t1_lista, ax1_lista, vx1_lista, x1_lista = ho1.preciznost()
t2_lista, ax2_lista, vx2_lista, x2_lista = ho2.preciznost()


fig, axes = plt.subplots(1, 3, figsize=(13, 4))

axes[0].plot(t1_lista, x1_lista)
axes[0].scatter(t2_lista, x2_lista, color="m")
axes[0].set_title("x-t graf")
axes[0].set_ylabel('put (m)')
axes[0].set_xlabel('vrijeme (s)')

axes[1].plot(t1_lista, vx1_lista)
axes[1].scatter(t2_lista, vx2_lista, color="m")
axes[1].set_title("v-t graf")
axes[1].set_ylabel('brzina (m/s)')
axes[1].set_xlabel('vrijeme (s)')

axes[2].plot(t1_lista, ax1_lista)
axes[2].scatter(t2_lista, ax2_lista, color="m")
axes[2].set_title("a-t graf")
axes[2].set_ylabel('akceleracija (m/s^2)')
axes[2].set_xlabel('vrijeme (s)')

plt.show()