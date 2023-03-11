from matplotlib import pyplot as plt


def ejercicio2():

    tf = 200
    t = 0
    mov_x = []
    mov_y = []
    mov_z = []

    while t < tf:
        mov_x.append(1)
        mov_y.append(4 * t ** 2)
        mov_z.append(t)
        t += 0.1

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    ax.plot3D(mov_x, mov_y, mov_z)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


if __name__ == "__main__":
    pass
