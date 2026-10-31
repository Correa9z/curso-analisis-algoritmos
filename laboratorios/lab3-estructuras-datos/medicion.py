"""Medicion del tiempo de busqueda de ListaEnlazada y TablaHash."""

import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS_N = [100, 500, 1000, 5000, 20000, 50000]
ALFAS_OBJETIVO = [0.5, 1, 2, 4, 10]
N_FIJO_EXPERIMENTO_B = 20000
CANTIDAD_INEXISTENTES = 200
CANTIDAD_INEXISTENTES_EXPERIMENTO_B = 3000
SEMILLA_GUIAS = 42
REPETICIONES = 9


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias_existentes(cantidad: int, semilla: int) -> list[int]:
    """Genera un lote de guias de diez digitos, todas distintas entre si.

    Args:
        cantidad: cuantas guias generar.
        semilla: semilla del generador aleatorio, para reproducibilidad.

    Returns:
        Lista de `cantidad` enteros distintos de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10 - 1), cantidad)


def es_primo(numero: int) -> bool:
    """Prueba primalidad por division, para elegir el tamano de la tabla.

    Args:
        numero: entero a evaluar.

    Returns:
        True si numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    if numero % 2 == 0:
        return numero == 2
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor objetivo.

    Explora alternadamente hacia arriba y hacia abajo desde el objetivo,
    y en caso de empate prefiere el de arriba.

    Args:
        objetivo: valor alrededor del cual se busca un primo.

    Returns:
        El primo encontrado mas cercano a objetivo.
    """
    objetivo = max(objetivo, 2)
    desplazamiento = 0
    while True:
        candidato_arriba = objetivo + desplazamiento
        if es_primo(candidato_arriba):
            return candidato_arriba
        candidato_abajo = objetivo - desplazamiento
        if candidato_abajo >= 2 and es_primo(candidato_abajo):
            return candidato_abajo
        desplazamiento += 1


def tiempo_promedio_busqueda(
    estructura: ListaEnlazada | TablaHash,
    guias_a_buscar: list[int],
    repeticiones: int = REPETICIONES,
) -> float:
    """Mide el tiempo promedio de busqueda sobre un lote de guias.

    Repite el lote completo varias veces y toma el lote mas rapido: el
    ruido del sistema operativo solo puede alargar una corrida, nunca
    acortarla, asi que el minimo es el que mejor refleja el costo real.

    Args:
        estructura: lista enlazada o tabla hash ya construida.
        guias_a_buscar: guias a buscar (tipicamente inexistentes).
        repeticiones: cuantas veces se repite el lote completo.

    Returns:
        Tiempo promedio por busqueda, en segundos.
    """
    tiempos_lote = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in guias_a_buscar:
            estructura.buscar(guia)
        tiempos_lote.append(time.perf_counter() - inicio)
    return min(tiempos_lote) / len(guias_a_buscar)


def experimento_lista_vs_tabla() -> tuple[list[float], list[float]]:
    """Mide el tiempo de busqueda de guias inexistentes vs. n.

    Returns:
        Una tupla (tiempos_lista, tiempos_tabla), en el mismo orden de
        TAMANOS_N.
    """
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    print("Experimento A: lista enlazada vs. tabla hash")
    print(f"{'n':>8}{'m':>8}{'alfa':>8}{'t. lista (s)':>18}{'t. tabla (s)':>18}")
    for n in TAMANOS_N:
        guias = generar_guias_existentes(n, SEMILLA_GUIAS)
        m = primo_cercano(n // 2)

        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        muestra = random.Random(1).sample(guias, min(30, n))
        for guia in muestra:
            assert lista.buscar(guia) == "en bodega"
            assert tabla.buscar(guia) == "en bodega"

        inexistentes = generar_guias_inexistentes(set(guias), CANTIDAD_INEXISTENTES)

        tiempo_lista = tiempo_promedio_busqueda(lista, inexistentes)
        tiempo_tabla = tiempo_promedio_busqueda(tabla, inexistentes)
        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        alfa = tabla.factor_carga()
        print(f"{n:>8}{m:>8}{alfa:>8.2f}{tiempo_lista:>18.8f}{tiempo_tabla:>18.8f}")

    plt.figure(figsize=(7, 5))
    plt.plot(TAMANOS_N, tiempos_lista, marker="o", label="lista enlazada")
    plt.plot(TAMANOS_N, tiempos_tabla, marker="o", label="tabla hash")
    plt.yscale("log")
    plt.title("Busqueda de guia inexistente: tiempo vs. numero de guias")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo promedio por busqueda (segundos, escala logaritmica)")
    plt.legend()
    plt.grid(True, alpha=0.3, which="both")
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()

    return tiempos_lista, tiempos_tabla


def experimento_factor_carga() -> tuple[list[float], list[float]]:
    """Mide el tiempo de busqueda de guias inexistentes vs. factor de carga.

    Usa mas guias inexistentes por lote que el experimento A, porque
    una busqueda en la tabla es tan rapida (del orden de un microsegundo
    o menos) que 200 por lote no alcanzan a dar una lectura estable del
    reloj del sistema.

    Returns:
        Una tupla (alfas_reales, tiempos), con el factor de carga real
        de cada tabla construida y el tiempo medido en ella.
    """
    guias = generar_guias_existentes(N_FIJO_EXPERIMENTO_B, SEMILLA_GUIAS)
    inexistentes = generar_guias_inexistentes(
        set(guias), CANTIDAD_INEXISTENTES_EXPERIMENTO_B
    )

    alfas_reales: list[float] = []
    tiempos: list[float] = []

    print("\nExperimento B: tiempo de busqueda vs. factor de carga (n = 20000)")
    print(f"{'m':>8}{'alfa':>10}{'t. tabla (s)':>18}")
    for alfa_objetivo in ALFAS_OBJETIVO:
        m = primo_cercano(max(1, round(N_FIJO_EXPERIMENTO_B / alfa_objetivo)))
        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en bodega")

        alfa_real = tabla.factor_carga()
        tiempo = tiempo_promedio_busqueda(tabla, inexistentes)
        alfas_reales.append(alfa_real)
        tiempos.append(tiempo)
        print(f"{m:>8}{alfa_real:>10.3f}{tiempo:>18.8f}")

    plt.figure(figsize=(7, 5))
    plt.plot(alfas_reales, tiempos, marker="o", label="tabla hash")
    plt.title("Tabla hash: tiempo de busqueda vs. factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo promedio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()

    return alfas_reales, tiempos


def main() -> None:
    """Ejecuta los dos experimentos de medicion del Laboratorio 3."""
    experimento_lista_vs_tabla()
    experimento_factor_carga()


if __name__ == "__main__":
    main()
