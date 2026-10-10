"""Experimento de la Parte 4: validacion experimental de la complejidad.

Compara el tiempo de ejecucion de insertion_sort y merge_sort sobre el
escenario A de Tamiza, para los mismos tamanos de entrada de la Parte 3.
"""

import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ALGORITMOS = {
    "insertion sort": insertion_sort,
    "merge sort": merge_sort,
}


def medir(algoritmo, n: int) -> float:
    tiempos = []
    for _ in range(REPETICIONES):
        datos = generar_aleatorio(n)
        inicio = time.perf_counter()
        algoritmo(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
    resultados: dict[str, list[float]] = {nombre: [] for nombre in ALGORITMOS}

    print(f"{'algoritmo':<18}{'n':>8}{'tiempo (s)':>14}")
    for nombre, algoritmo in ALGORITMOS.items():
        for n in TAMANOS:
            tiempo = medir(algoritmo, n)
            resultados[nombre].append(tiempo)
            print(f"{nombre:<18}{n:>8}{tiempo:>14.5f}")

    plt.figure(figsize=(7, 5))
    for nombre in ALGORITMOS:
        plt.plot(TAMANOS, resultados[nombre], marker="o", label=nombre)
    plt.title("Insertion sort vs. merge sort: tiempo vs. tamano de entrada (escenario A)")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
