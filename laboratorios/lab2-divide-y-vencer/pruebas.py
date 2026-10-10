"""Pruebas de verificacion del subarreglo maximo (fuerza bruta vs. divide y venceras)."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def verificar_suma_esperada(valores: list[float], suma_esperada: float) -> None:
    """Corre ambos algoritmos sobre una serie y valida la suma esperada.

    Args:
        valores: serie de prueba.
        suma_esperada: suma que debe dar el mejor tramo en esa serie.
    """
    _, _, suma_bruta = subarreglo_fuerza_bruta(valores)
    _, _, suma_dyv = subarreglo_maximo(valores, 0, len(valores) - 1)
    assert suma_bruta == suma_esperada, (
        f"fuerza bruta dio {suma_bruta}, se esperaba {suma_esperada}"
    )
    assert suma_dyv == suma_esperada, (
        f"divide y venceras dio {suma_dyv}, se esperaba {suma_esperada}"
    )


def verificar_coinciden(valores: list[float]) -> None:
    """Corre ambos algoritmos sobre una serie y valida que coincidan entre si.

    Args:
        valores: serie de prueba.
    """
    _, _, suma_bruta = subarreglo_fuerza_bruta(valores)
    _, _, suma_dyv = subarreglo_maximo(valores, 0, len(valores) - 1)
    assert suma_bruta == suma_dyv, (
        f"las dos soluciones no coinciden: {suma_bruta} != {suma_dyv}"
    )


def main() -> None:
    """Ejecuta los casos de prueba del Laboratorio 2."""
    serie_del_enunciado = [-3, 5, -2, 8, -6, 3, 9, -4]
    verificar_suma_esperada(serie_del_enunciado, 17)

    un_solo_elemento_positivo = [7]
    verificar_suma_esperada(un_solo_elemento_positivo, 7)

    un_solo_elemento_negativo = [-7]
    verificar_suma_esperada(un_solo_elemento_negativo, -7)

    todos_negativos = [-5, -2, -8, -1, -9]
    verificar_suma_esperada(todos_negativos, -1)

    todos_positivos = [2, 4, 1, 3, 6]
    verificar_suma_esperada(todos_positivos, 16)

    # el mejor tramo (4, -1, 2, 1) cruza el punto medio de la lista
    mejor_tramo_cruzado = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    verificar_suma_esperada(mejor_tramo_cruzado, 6)

    generador = random.Random(7)
    for _ in range(25):
        tamano = generador.randint(2, 60)
        valores_aleatorios = [generador.randint(-100, 100) for _ in range(tamano)]
        verificar_coinciden(valores_aleatorios)

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()
