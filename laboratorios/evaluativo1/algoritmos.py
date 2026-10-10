"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor, que es el orden que Tamiza necesita para
    generar la lista de llamadas. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0

    for i in range(1, len(resultado)):
        clave = resultado[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if resultado[j] < clave:
                resultado[j + 1] = resultado[j]
                j -= 1
            else:
                break
        resultado[j + 1] = clave

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor, que es el orden que Tamiza necesita para
    generar la lista de llamadas. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = 0

    def dividir(arreglo: list[int]) -> list[int]:
        if len(arreglo) <= 1:
            return arreglo
        medio = len(arreglo) // 2
        izquierda = dividir(arreglo[:medio])
        derecha = dividir(arreglo[medio:])
        return combinar(izquierda, derecha)

    def combinar(izquierda: list[int], derecha: list[int]) -> list[int]:
        nonlocal comparaciones
        fusionado: list[int] = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if izquierda[i] >= derecha[j]:
                fusionado.append(izquierda[i])
                i += 1
            else:
                fusionado.append(derecha[j])
                j += 1
        fusionado.extend(izquierda[i:])
        fusionado.extend(derecha[j:])
        return fusionado

    ordenado = dividir(list(datos))
    return ordenado, comparaciones
