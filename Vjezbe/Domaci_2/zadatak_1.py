import zadatak as z


def const_force(v, x, t):
    return 50 


def elastic_force(v, x, t):
    k = 10
    return -k*x


p1 = z.Force(20, 2, 0.01, const_force)
p1.set_initial_conditions(0, 10, 0, 10, 2, 0.1, const_force)
p1.graf()


p2 = z.Force(20, 2, 0.01, elastic_force)
p2.set_initial_conditions(0, 10, 0, 10, 2, 0.1, elastic_force)
p2.graf()