"""Experimento de la Parte 3: peor caso, mejor caso y caso promedio.

Ejecuta insertion_sort sobre los tres escenarios de Tamiza (aleatorio,
casi ordenado e inverso), para una serie de tamanos de entrada, y
genera las graficas de comparaciones y de tiempo de ejecucion.
"""

import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - aleatorio": generar_aleatorio,
    "B - casi ordenado": generar_casi_ordenado,
    "C - orden inverso": generar_inverso,
}


def medir(generador, n: int) -> tuple[float, int]:
    """Corre insertion_sort varias veces sobre un lote y promedia."""
    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        datos = generador(n)
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        tiempos.append(time.perf_counter() - inicio)

    return statistics.median(tiempos), comparaciones


def main() -> None:
    resultados: dict[str, dict[str, list[float]]] = {
        nombre: {"tiempo": [], "comparaciones": []} for nombre in ESCENARIOS
    }

    print(f"{'escenario':<20}{'n':>8}{'tiempo (s)':>14}{'comparaciones':>16}")
    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir(generador, n)
            resultados[nombre]["tiempo"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(f"{nombre:<20}{n:>8}{tiempo:>14.5f}{comparaciones:>16}")

    plt.figure(figsize=(7, 5))
    for nombre in ESCENARIOS:
        plt.plot(TAMANOS, resultados[nombre]["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 5))
    for nombre in ESCENARIOS:
        plt.plot(TAMANOS, resultados[nombre]["tiempo"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
