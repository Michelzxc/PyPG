import random as ran
import secrets as sec
import matplotlib.pyplot as plt


def introduccion_a_plt() -> None:
    """Introduccion a matplotlib.pyplot."""

    tamano = 400

    valores_x = [n for n in range(tamano)]
    valores_y_ran = [ran.choice(valores_x) for n in range(tamano)]
    valores_y_sec = [sec.choice(valores_x) for n in range(tamano)]

    plt.subplot(2, 1, 1)
    plt.plot(valores_x, valores_y_ran, linewidth=1)
    plt.grid()
    plt.ylabel("random")

    plt.subplot(2, 1, 2)
    plt.plot(valores_x, valores_y_sec, linewidth=1)
    plt.ylabel("secrets")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    introduccion_a_plt()
