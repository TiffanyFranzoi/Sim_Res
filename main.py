import numpy as np
import matplotlib.pyplot as plt
from solucoes import Solucoes
from graficos import (
    grafico_radial_inf,
    grafico_linear_alimentacao_externa,
    grafico_linear_infinito,
)


def main():
    # Cria uma instância da classe Solucoes com os parâmetros especificados
    case_1 = Solucoes(
        Po=500, Pw=200, qw=5, mi=2, k=100, h=5, phi=0.25, ct=9e-9, L=500, A=1000
    )

    # Define as faixas de valores para as variáveis independentes
    r_radial_infinito = np.linspace(1, 100)
    t_radial_infinito = np.linspace(0, 500, 6)

    x_linear_alimext = np.linspace(1, 500)
    t_linear_alimext = np.linspace(0, 1000, 6)

    x_linear_infinito = np.linspace(1, 15000000)
    t_linear_infinito = np.linspace(0, 500, 6)

    # Cria uma única janela para todos os gráficos
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    plt.subplots_adjust(wspace=0.5)  # Espaçamento entre os gráficos

    # Plota os gráficos na janela
    grafico_radial_inf(case_1, r_radial_infinito, t_radial_infinito, ax=axes[0])
    grafico_linear_alimentacao_externa(case_1, x_linear_alimext, t_linear_alimext, ax=axes[1])
    grafico_linear_infinito(case_1, x_linear_infinito, t_linear_infinito, ax=axes[2])

    plt.show()


if __name__ == "__main__":
    main()
