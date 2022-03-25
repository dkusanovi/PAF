import particle as prt
import matplotlib.pyplot as plt
import numpy as np

# graf ovisnoti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka ∆t



def graf():
    p1 = prt.Particle(10, 60, 0, 0)
    dt = []
    relative_error = []


    for i in range(100):
        # p1 = prt.Particle(10, 60, 0, 0)
        p1.set_initial_conditions(10, 60, 0, 0)
        dt_br = i*0.001 + 0.001
        dt.append(dt_br)
        reach_a = p1.analitical()
        reach_n = p1.range(dt_br)
        err = ((abs(reach_a - reach_n))/reach_a)*100
        relative_error.append(err)
        p1.reset()

    # fig, ax = plt.subplots()
    plt.xlabel("dt [s]")
    plt.ylabel("Absolute relative error [%]")
    plt.title("Absolute relative error for range of projectile")
    plt.plot(dt, relative_error)
    plt.show()

graf()