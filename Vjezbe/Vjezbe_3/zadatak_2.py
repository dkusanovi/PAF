import particle as prt
import matplotlib.pyplot as plt
import numpy as np

# graf ovisnoti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka ∆t



def graf():
    p1 = prt.Particle(10, 60, 0, 0)
    #p1.set_initial_conditions(10, 60, 0, 0)
    dt = []
    dt_br = 0.01
    dt.append(dt_br)
    relative_error = []


    for i in range(100):
        dt_br = dt_br + 0.01
        dt.append(dt_br)


    for i in range(101):
        p1 = prt.Particle(10, 60, 0, 0)
        p1.set_initial_conditions(10, 60, 0, 0)
        reach_a = p1.analitical()
        reach_n = p1.range(dt_br)
        err = ((abs(reach_a - reach_n))/reach_a)*0.01
        relative_error.append(err)


    #fig, ax = plt.subplots()
    plt.xlabel("dt [s]")
    plt.ylabel("Absolute relative error [%]")
    plt.title("Absolute relative error for range of projectile")
    plt.plot(dt, relative_error)
    plt.show()

graf()