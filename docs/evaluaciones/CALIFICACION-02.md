# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juan Pablo Correa · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `7e6fda3`

Muy buen trabajo: el laboratorio está completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre n = 10 y n = 50 y lo explica con el costo fijo de la recursión.
- Compara con el máximo de un arreglo: combinar cuesta una comparación, la recurrencia da O(n) y dividir no aporta. La conclusión sobre el costo de combinar es clara.
- Recomienda divide y vencerás y estima 9.7 horas contra unos 3 segundos para 1.000.000 de registros, declarando que son estimaciones y sin regla de tres lineal.

**Lo que puede mejorar:**
- Al explicar el cruce en tamaños pequeños, apóyese también en más de dos puntos de la gráfica (por ejemplo n = 100) para mostrar que la ventaja se mantiene.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + O(n)` y explica de dónde sale cada término, incluido el costo lineal del caso cruzado.
- Aplica el método maestro (a = 2, b = 2) y justifica la fuerza bruta con la suma n + (n-1) + ... + 1.

**Lo que puede mejorar:**
- Use Θ en lugar de O cuando el resultado es exacto, y diga la condición del caso con precisión: f(n) = Θ(n^(log₂2)) = Θ(n), por eso el resultado es Θ(n log n).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en las listas aleatorias; `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- Ninguna función cambia la lista recibida; el código cumple PEP 8, con type hints y docstrings en cada función.
- `pruebas.py` cubre todos los casos pedidos y 25 listas aleatorias.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados, leyenda y ocho tamaños. Las cifras del informe (por ejemplo 2.239 s y 0.0157 s en n = 8000) coinciden con la gráfica.
- Calcula el factor al duplicar n para cada algoritmo y lo compara con lo esperado.

**Lo que puede mejorar:**
- Un factor de 3.6 para la fuerza bruta es algo menor que 4; conviene decirlo y explicar por qué (ruido, efectos de memoria) en vez de afirmar solo que "coincide".
- Calcule el factor en más de una pareja de tamaños, o agregue una tabla con los valores medidos, para que la conclusión sea más firme.
- Calcule el factor esperado de n log n al duplicar (cerca de 2.1) para compararlo con el 2.2 medido.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta `laboratorios/lab2-divide-y-vencer/` en la ubicación acordada, con todos los archivos del entregable.
- El README sigue el orden pedido, enlaza el código de cada parte, incrusta la gráfica con ruta que funciona y trae las instrucciones de reproducción.
- Hay tres commits del laboratorio con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones coinciden con una referencia en listas aleatorias y la medición corre sin errores y genera la gráfica.

## Para el próximo laboratorio
- Use Θ cuando el resultado de la recurrencia sea exacto y cite la condición del caso del método maestro completa.
- Cuando un factor medido no coincida del todo con la teoría, explique la diferencia en lugar de decir solo que coincide.
- Incluya una tabla con los tiempos medidos y calcule factores en varias parejas de tamaños.
- Mantenga el ritmo de commits pequeños y descriptivos.
