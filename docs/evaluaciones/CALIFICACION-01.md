# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Pablo Correa Buitrago · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `dd54425`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue con claridad entre que el algoritmo sea correcto y que sea rápido, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica bien por qué un servidor del doble de velocidad no arregla el problema: el trabajo crece con el cuadrado de los datos.
- Su segundo ejemplo (las fotos de respaldo) es propio, con cantidades y con la restricción que se rompe.
- En la parte ética identifica perjuicios concretos para el paciente y para el operador del centro de contacto, y discute que el orden de la lista exige exactitud, no solo rapidez.

**Lo que puede mejorar:**
- En lo ambiental explica la idea (más tiempo, más energía, todas las noches), pero no pone ninguna cifra ni estimación del gasto acumulado.
- El segundo perjuicio (que alguien recorte la lista) es una suposición; quedaría más fuerte con un caso que ya ocurre en el problema.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, justifica que usaría el peor caso por la ventana estricta y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro verificando que se cumple el caso que aplica.
- Presenta la tabla de complejidades por caso.

**Lo que puede mejorar:**
- En insertion sort indica cuántas veces corre cada línea, pero no le asigna un costo a cada una ni muestra la suma completa; el resultado queda explicado en palabras más que calculado.
- El caso promedio se afirma (`tᵢ ≈ i/2`) sin mostrar la cuenta.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor, declarado), no cambian la lista recibida y cuentan solo comparaciones entre elementos. En una lista ya ordenada insertion sort cuenta exactamente n − 1.
- `merge_sort` tiene su propia mezcla recursiva.
- Los generadores producen valores distintos, del tamaño pedido y con semilla.
- El código cumple el estilo PEP 8.

**Lo que puede mejorar:**
- `generar_casi_ordenado` usa `sorted()` para armar el 98 % ordenado. No está dentro de los algoritmos, pero el laboratorio prohíbe usar ordenamientos de Python; debía construir esa parte sin ellos.
- Varias funciones no tienen docstring ni todos sus tipos: `medir` (en las dos partes), `main`, y las funciones internas `dividir` y `combinar`.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y las curvas pedidas en los mismos ejes.
- Identifica con cifras que C es el peor caso, B el mejor y A el promedio, y lo contrasta con su predicción.
- Describe lo que hace cada curva en la gráfica de insertion sort contra merge sort y lo compara con las complejidades calculadas; explica el tamaño pequeño.
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros declarándolo estimación y responde a la propuesta del servidor con un dato medido. También discute la memoria extra.

**Lo que puede mejorar:**
- En la gráfica de tiempo, la curva de merge sort queda pegada al fondo y no se ve su forma; una escala logarítmica ayudaría.
- Los ejes dicen "n" sin unidad de registros. El estimado de merge sort (4,5 s) no coincide del todo con su propia cuenta; revise el cálculo.

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- El informe está organizado por partes, con instrucciones para reproducir, las gráficas visibles y enlaces al código en las Partes 3 y 4.

**Lo que puede mejorar:**
- No siguió la estructura acordada: el trabajo está en la rama `dev` (llegó por un Pull Request desde `lab1`) y la rama principal, que se llama `master` y no `main`, no lo contiene. Debía subirlo a la rama `main`.
- La carpeta se llama `laboratorios/evaluativo1/` y debía llamarse `lab1-fundamentos-complejidad-recurrencias` (dentro de `laboratorios/`).
- Solo hay un commit con el trabajo del laboratorio; se pedían al menos cinco commits descriptivos que muestren el avance.
- Se subió además un archivo `Realizar.md` (copia del enunciado) que no hace parte del entregable.
- Escribió "Juan Correa" en lugar de su nombre completo.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en mis pruebas, los scripts de las Partes 3 y 4 corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Suba el trabajo a la rama `main` y use exactamente el nombre de carpeta acordado.
- Haga commits pequeños y frecuentes (al menos cinco) con mensajes que digan qué se hizo.
- Ponga docstring y tipos en todas las funciones, incluidas las auxiliares.
- No use `sorted()` ni `sort()` en ninguna parte del código; arme los datos de prueba sin ellos.
- Al explicar costos, muestre la cuenta completa y agregue cifras a los argumentos (por ejemplo, el consumo de energía).
