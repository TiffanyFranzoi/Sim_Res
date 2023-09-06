import matplotlib.pyplot as plt


def grafico_radial_inf(solucao, r, t, ax=None):
    """
    Gera um gráfico de fluxo radial em um reservatório infinito.

    Args:
        solucao (Solucoes): Objeto contendo os parâmetros do reservatório.
        r (array): Array de distâncias radiais.
        t (array): Array de tempos.
        ax (Axes, opcional): Eixo para plotagem. Se não for especificado, um novo gráfico será criado.

    Returns:
        None
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Calcula a pressão radial
    p = solucao.pressao_radial_inf(r, t)

    # Plota os resultados
    for P in p:
        ax.plot(r, P)

    # Configuração do gráfico
    ax.set_xlabel("Raio", fontsize=12)
    ax.set_ylabel("Pressão", fontsize=12)
    ax.set_title("Fluxo radial - Reservatório infinito", fontsize=15)
    ax.grid()


def grafico_linear_alimentacao_externa(solucao, x, t, ax=None):
    """
    Gera um gráfico de fluxo linear com alimentação externa.

    Args:
        solucao (Solucoes): Objeto contendo os parâmetros do reservatório.
        x (array): Array de posições.
        t (array): Array de tempos.
        ax (Axes, opcional): Eixo para plotagem. Se não for especificado, um novo gráfico será criado.

    Returns:
        None
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Calcula a pressão linear com alimentação externa
    p = solucao.pressao_linear_alimentacao_externa(x, t)

    # Plota os resultados
    for P in p:
        ax.plot(x, P)

    # Configuração do gráfico
    ax.set_xlabel("Comprimento", fontsize=12)
    ax.set_ylabel("Pressão", fontsize=12)
    ax.set_title("Fluxo linear - Alimentação externa", fontsize=15)
    ax.grid()


def grafico_linear_infinito(solucao, x, t, ax=None):
    """
    Gera um gráfico de fluxo linear em um reservatório infinito.

    Args:
        solucao (Solucoes): Objeto contendo os parâmetros do reservatório.
        x (array): Array de posições.
        t (array): Array de tempos.
        ax (Axes, opcional): Eixo para plotagem. Se não for especificado, um novo gráfico será criado.

    Returns:
        None
    """
    if ax is None:
        fig, ax = plt.subplots()

    # Calcula a pressão linear em um reservatório infinito
    p = solucao.pressao_linear_infinito(x, t)

    # Plota os resultados
    for P in p:
        ax.plot(x, P)

    # Configuração do gráfico
    ax.set_xlabel("Comprimento", fontsize=12)
    ax.set_ylabel("Pressão", fontsize=12)
    ax.set_title("Fluxo linear - Reservatório infinito", fontsize=15)
    ax.grid()
