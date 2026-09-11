"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    generador = random.Random(semilla)
    return generador.sample(range(n * 10), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    generador = random.Random(semilla)
    valores = generador.sample(range(n * 10), n)

    corte = round(n * 0.98)
    parte_ordenada = sorted(valores[:corte], reverse=True)
    parte_nueva = valores[corte:]
    generador.shuffle(parte_nueva)

    return parte_ordenada + parte_nueva


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n))
