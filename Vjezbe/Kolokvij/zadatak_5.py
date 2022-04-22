import projectiledrop as pd
import numpy as np
import matplotlib.pyplot as plt

p1 = pd.ProjectileDrop(1000, 10)
p2 = pd.ProjectileDrop(1000, 10)
p3 = pd.ProjectileDrop(1000, 10)

p1.to_hit_target(3, 10, 0, 50, 0.1)
p2.to_hit_target(3, 10, 0, 0, 0.1)
p3.to_hit_target(3, 10, 0, -50, 0.1)

