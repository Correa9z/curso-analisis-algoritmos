"""Pruebas de verificacion de ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_busqueda_basica() -> None:
    """Verifica una busqueda exitosa y una infructuosa en ambas estructuras."""
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(1000000099) is None

    tabla = TablaHash(11)
    tabla.insertar(1000000010, "en bodega")
    tabla.insertar(1000000024, "en reparto")
    assert tabla.buscar(1000000024) == "en reparto"
    assert tabla.buscar(1000000099) is None


def probar_colision_forzada() -> None:
    """Verifica la colision de las guias 10, 24 y 17 con m = 7."""
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3
    assert tabla.casillas[3].tamano == 3

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(31) is None  # 31 % 7 tambien da 3, pero nunca se inserto

    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara lista y tabla sobre colecciones aleatorias, con y sin la guia."""
    generador = random.Random(11)
    for _ in range(20):
        cantidad = generador.randint(5, 80)
        guias = generador.sample(range(10**9, 10**10 - 1), cantidad)
        guias_usadas = set(guias)

        lista = ListaEnlazada()
        tabla = TablaHash(generador.choice((7, 11, 17, 31)))
        for guia in guias:
            estado = generador.choice(("en bodega", "en reparto", "entregado"))
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        guia_inexistente = max(guias) + 1
        while guia_inexistente in guias_usadas:
            guia_inexistente += 1
        assert lista.buscar(guia_inexistente) is None
        assert tabla.buscar(guia_inexistente) is None


def main() -> None:
    """Ejecuta los casos de prueba del Laboratorio 3."""
    probar_busqueda_basica()
    probar_colision_forzada()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()
