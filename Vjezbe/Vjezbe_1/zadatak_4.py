x1 = float(input("x os: "))
y1 = float(input("y os: "))
x2 = float(input("x os: "))
y2 = float(input("y os: "))


def koordinate():

    k = (y2-y1)/(x2-x1)
    l = -k*x1 -y1

    if l < 0:
        print("y = " , k, "x " , l)
    else:
        print("y = " , k, "x +" , l)

    return k, l

koordinate()