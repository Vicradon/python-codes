import turtle as t
t.speed(0)


def rect(w, h):
        for i in range(2):
                t.fd(w)
                t.lt(90)
                t.fd(h)
                t.lt(90)


def recursiveSquares(width, height, padding):


        dummyHeight = height//8

        for i in range(dummyHeight):
                rect(width, height)

                t.pu()
                t.fd(padding)
                t.lt(90)
                t.fd(padding)
                t.rt(90)
                t.pd()

                width -= padding*2
                height -= padding*2


        t.ht()

recursiveSquares(200, 100, 12)
