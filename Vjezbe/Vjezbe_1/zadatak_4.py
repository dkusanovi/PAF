x1 = 15
y1 = 4
x2 = 20
y2 = 3


def koordinate():

    k = (y2-y1)/(x2-x1)
    l = -k*x1 + y1

    if l < 0:
        print("y = " , k, "x " , l)
    else:
        print("y = " , k, "x +" , l)

    return k, l

koordinate()