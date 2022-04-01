import particle as prt
import numpy as np
import matplotlib.pyplot as plt


p1 = prt.Particle(10, 40, 0, 0)

p1.set_initial_conditions(10, 40, 0, 0)

p1.max_speed()

p1.total_time()

p1.velocity_to_hit_target(8, 5, 17, 0.01)

p1.angle_to_hit_target(8, 5, 17, 0.01)