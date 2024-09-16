# LAB1_OPTI
Laboratorio 1: experimentos con problemas de optimización

Fecha de entrega: lunes 16 de septiembre
Modalidad de entrega: socialización en clase y repositorio en Git-Hub.
Integrantes: Gabriela Moreno - Santiago Romero - Fabián Pallares.
Objetivo: Validar de manera práctica los conceptos básicos de optimización.

1. Escoge un problema de optimización de dos variables (o puedes crear uno también). Plantea su función de costo y las restricciones. Grafica la región factible con ayuda de Python. Desarrolla un programa que le permita al usuario:
tener el valor de la función de costo a partir de un punto (x,y)
ver gráficamente cómo cambia la región factible ante un cambio en las restricciones.

*Ejercicio Seleccionado*
Maximizar el beneficio de vender dos productos A y B donde el beneficio por unidad de A es de 3 y el de B es de 2.
Tener en cuenta que solo se producen hasta 100 unidades en total y no se pueden producir cantidades negativas.

Resuelto en el Google Colab.

2. Selecciona un método de representación de matrices sparse e impleméntalo en Python desde cero. Compara tus resultados con la función de las librerías de Python.
Resuelto en el Google colab


3. Crea un programa para implementar la expansión en series de Taylor. El usuario debe ingresar la cantidad de términos de la expansión, el punto de expansión y la función a representar (debe tener al menos 5 funciones diferentes para escoger). Se debe mostrar en una gráfica la función original y la aproximación.

Resuelto en el Google Colab






4. Escoge 3 algoritmos de optimización sin restricciones. Realiza cambios sobre sus parámetros y sobre el punto inicial. ¿Cómo afectan estos cambios los resultados? ¿Cómo afecta el tiempo de convergencia o cantidad de iteraciones? Nota: Puedes utilizar las librerías de Python y alguna ayuda gráfica o tabulaciones si lo necesitan para soportar sus conclusiones.

Algoritmos a evaluar:
- Gradiente Descendente: Es un método de optimización basado en la primera derivada que minimiza una función moviéndose en la dirección opuesta a su gradiente.
- Newton-Raphson: Utiliza tanto la primera como la segunda derivada (Hessiana) para realizar un ajuste cuadrático local de la función y encontrar puntos mínimos de manera más eficiente.
- Quasi-Newton (BFGS): Aproxima la matriz Hessiana sin tener que calcularla directamente, lo que lo hace más eficiente que Newton-Raphson para grandes problemas.

  
Factores a cambiar:
Punto inicial: Este valor puede influir significativamente en la rapidez con que los algoritmos convergen y si alcanzan un mínimo global o local.
Parámetros del algoritmo: Principalmente, la tasa de aprendizaje (para el Gradiente Descendente) y el criterio de convergencia (tolerancia).
Voy a proceder a implementar estos algoritmos y graficar los resultados cambiando tanto el punto inicial como los parámetros.
Implementación
Voy a implementar los algoritmos y luego realizaré los experimentos para ver cómo estos cambios afectan el desempeño.
Aquí están los resultados obtenidos al comparar los tres algoritmos de optimización sin restricciones (BFGS, Newton-Raphson y Gradiente Conjugado) utilizando diferentes puntos iniciales:

![image](https://github.com/user-attachments/assets/96275f0a-dcfc-4675-99fd-2cda5bf91a36)


Observaciones:
1. Convergencia:
BFGS y Newton-CG convergen a valores muy cercanos al mínimo de la función (en torno a 10−1510^{-15}10−15), mostrando buena precisión en ambos casos.
CG (Gradiente Conjugado) tiene una precisión ligeramente inferior, pero aún es aceptable.
2. Iteraciones:
Newton-CG necesitó muchas más iteraciones para el punto inicial lejano (-1.2, 1.0), aunque con el punto inicial más cercano (2.0, 2.0) fue más eficiente.
BFGS fue más estable en términos de iteraciones para ambos puntos iniciales.
CG fue el más rápido en términos de iteraciones cuando el punto inicial estaba más cerca del mínimo (2.0, 2.0).
3. Tiempo de ejecución:
BFGS fue el más eficiente en términos de tiempo, seguido de cerca por CG, mientras que Newton-CG fue el más lento, particularmente para el punto inicial más alejado.

Conclusiones:
Cambiar el punto inicial puede afectar significativamente la cantidad de iteraciones, especialmente en el caso de Newton-CG.
Los parámetros del algoritmo, como la tolerancia o la tasa de aprendizaje, también juegan un papel importante en la convergencia, aunque no se cambiaron explícitamente aquí.
BFGS parece ser el algoritmo más estable en términos de tiempo y número de iteraciones, mientras que Newton-CG puede ser más sensible a la ubicación del punto inicia

