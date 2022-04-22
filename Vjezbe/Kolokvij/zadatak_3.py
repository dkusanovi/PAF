import projectiledrop as pd
import matplotlib.pyplot as plt


p1 = pd.ProjectileDrop(2000, 200)


t_lista, vy_lista, vx_lista, y_lista, x_lista = p1.euler(0.01)


def graf():
    fig, axes = plt.subplots(1, 2, figsize=(14, 4))

    axes[0].plot(y_lista, x_lista)
    axes[0].set(ylabel="x koordinata", xlabel="y koordinata")
    axes[0].set_title("Graf ovisnsti puta o visini")

    axes[1].plot(t_lista, vy_lista)
    axes[1].set(ylabel="vertikalna brzina", xlabel="vrijeme")
    axes[1].set_title("Graf ovisnsti brzine o vremenu")

    plt.show()


graf()
