"""Medicion del tiempo de ejecucion de ambas soluciones del subarreglo maximo."""

import random
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 7
SEMILLA = 123


def generar_serie(n: int, semilla: int) -> list[int]:
    """Genera una serie de variaciones diarias de caja.

    Args:
        n: cantidad de dias de la serie.
        semilla: semilla del generador aleatorio, para que la medicion
            sea reproducible.

    Returns:
        Lista de n enteros entre -100 y 100 (inclusive).
    """
    generador = random.Random(semilla)
    return [generador.randint(-100, 100) for _ in range(n)]


def medir_fuerza_bruta(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de la fuerza bruta sobre una serie.

    Args:
        valores: serie sobre la que se corre el algoritmo.

    Returns:
        El menor tiempo de ejecucion, en segundos, de REPETICIONES
        corridas. Se toma el minimo y no el promedio porque el ruido
        del sistema operativo solo puede hacer que una corrida tarde
        mas, nunca menos, de lo que realmente cuesta el algoritmo.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        subarreglo_fuerza_bruta(valores)
        tiempos.append(time.perf_counter() - inicio)
    return min(tiempos)


def medir_divide_y_venceras(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de divide y venceras sobre una serie.

    Args:
        valores: serie sobre la que se corre el algoritmo.

    Returns:
        El menor tiempo de ejecucion, en segundos, de REPETICIONES
        corridas, por la misma razon que en medir_fuerza_bruta.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        subarreglo_maximo(valores, 0, len(valores) - 1)
        tiempos.append(time.perf_counter() - inicio)
    return min(tiempos)


def main() -> None:
    """Ejecuta el experimento de medicion y genera la grafica del laboratorio 2."""
    tiempos_bruta: list[float] = []
    tiempos_dyv: list[float] = []

    print(f"{'n':>8}{'fuerza bruta (s)':>20}{'divide y venceras (s)':>24}")
    for n in TAMANOS:
        valores = generar_serie(n, SEMILLA)

        _, _, suma_bruta = subarreglo_fuerza_bruta(valores)
        _, _, suma_dyv = subarreglo_maximo(valores, 0, n - 1)
        assert suma_bruta == suma_dyv, (
            f"las dos soluciones no coinciden para n={n}: {suma_bruta} != {suma_dyv}"
        )

        tiempo_bruta = medir_fuerza_bruta(valores)
        tiempo_dyv = medir_divide_y_venceras(valores)
        tiempos_bruta.append(tiempo_bruta)
        tiempos_dyv.append(tiempo_dyv)
        print(f"{n:>8}{tiempo_bruta:>20.6f}{tiempo_dyv:>24.6f}")

    plt.figure(figsize=(7, 5))
    plt.plot(TAMANOS, tiempos_bruta, marker="o", label="fuerza bruta")
    plt.plot(TAMANOS, tiempos_dyv, marker="o", label="divide y venceras")
    plt.yscale("log")
    plt.title("Subarreglo maximo: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos, escala logaritmica)")
    plt.legend()
    plt.grid(True, alpha=0.3, which="both")
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_n.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
