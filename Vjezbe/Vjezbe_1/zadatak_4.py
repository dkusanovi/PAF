def koordinate(x1, y1, x2, y2):

    k = (y2-y1)/(x2-x1)
    l = -k*x1 + y1

    if l < 0:
        print("y = " , k, "x " , l)
    else:
        print("y = " , k, "x +" , l)

    return k, l

koordinate(15, 4, 20, 3)