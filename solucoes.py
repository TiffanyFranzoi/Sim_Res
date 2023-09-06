import numpy as np
import scipy.special as sc


class Solucoes:
    def __init__(self, Po, Pw, qw, mi, k, h, phi, ct, L, A):
        # Inicialização dos parâmetros
        self.Po = Po  # Pressão inicial
        self.Pw = Pw  # Pressão no poço
        self.qw = qw  # Vazão do poço
        self.mi = mi  # Viscosidade do fluido
        self.k = k  # Permeabilidade
        self.h = h  # Espessura do reservatorio
        self.phi = phi  # Porosidade
        self.ct = ct  # Compressibilidade total
        self.L = L  # Comprimento do reservatório
        self.A = A  # Área de drenagem

    def pressao_radial_inf(self, r, t):
        """
        Calcula a pressão radial em um reservatório infinito.

        Args:
            r (array): Array de distâncias radiais.
            t (array): Array de tempos.

        Returns:
            list: Lista de pressões calculadas.
        """
        P = []
        P1 = (self.qw * self.mi) / (4 * np.pi * self.k * self.h)
        for t in t:
            # Cálculo da pressão radial
            p = self.Po + P1 * sc.expi(
                (self.phi * self.mi * self.ct * (r**2)) / (4 * self.k * t)
            )
            P.append(p)
        return P

    def pressao_linear_alimentacao_externa(self, x, t):
        """
        Calcula a pressão linear com alimentação externa.

        Args:
            x (array): Array de posições.
            t (array): Array de tempos.

        Returns:
            list: Lista de pressões calculadas.
        """
        soma = 0
        P = []
        eta = self.k / (self.phi * self.mi * self.ct)
        for t in t:
            for n in range(1, 100):
                # Cálculo da soma das séries
                soma += (
                    np.sin(n * np.pi * x / self.L)
                    * (1 / n)
                    * (np.e ** (-(eta * t) * (n * np.pi / self.L) ** 2))
                )
            soma *= 2 / np.pi
            # Cálculo da pressão linear com alimentação externa
            p = (self.Po - self.Pw) * (x / self.L + soma) + self.Pw
            P.append(p)
        return P

    def pressao_linear_infinito(self, x, t):
        """
        Calcula a pressão linear em um reservatório infinito.

        Args:
            x (array): Array de posições.
            t (array): Array de tempos.

        Returns:
            list: Lista de pressões calculadas.
        """
        P = []
        eta = self.k / (self.phi * self.mi * self.ct)
        P1 = (self.qw * self.mi * self.L) / (self.k * self.A)
        for t in t:
            # Cálculo da pressão linear em um reservatório infinito
            p = self.Po - P1 * (
                np.sqrt((4 * eta * t) / (np.pi * self.L**2))
                * np.e ** ((-(x**2)) / (4 * eta * t))
                - (x * sc.erfc(x / np.sqrt(4 * eta * t))) / self.L
            )
            P.append(p)
        return P
