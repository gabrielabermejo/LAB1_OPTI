import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Función de costo
def funcion_costo(a, b):
    return 3 * a + 2 * b

# Función para graficar la región factible
def graficar_region_factible(ax, restricciones_vertices):
    region = Polygon(restricciones_vertices, closed=True, fill=True, edgecolor='b', alpha=0.3)
    ax.add_patch(region)

    # Graficar las líneas de las restricciones
    x = np.linspace(0, 100, 400)
    
    # Restricción: A + B <= 100
    y1 = 100 - x
    ax.plot(x, y1, label='A + B = 100', color='r')
    
    # Restricción: A >= 0 (color verde)
    ax.axvline(x=0, color='g', linestyle='--', label='A = 0', linewidth=2)
    
    # Restricción: B >= 0 (color azul)
    ax.axhline(y=0, color='b', linestyle='--', label='B = 0', linewidth=2)

# Gráfico dinámico con restricciones variables
def graficar_con_restricciones(a, b, ajuste=100):
    # Configurando los límites de las restricciones
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Región Factible con Restricciones Ajustadas")

    # Vértices del área factible (triángulo formado por las restricciones)
    restricciones_vertices = [(0, 0), (100, 0), (0, 100)]

    # Graficando la región factible
    graficar_region_factible(ax, restricciones_vertices)
    
    # Graficar el punto ajustado
    ax.plot(a, b, 'ko', label=f'Ajuste: A={a}, B={b}')  # Punto negro

    # Mostrar mensaje si el ajuste está fuera de la región factible
    if a < 0 or b < 0 or a + b > ajuste:
        print("El punto ajustado NO hace parte de la región factible.")
        ax.text(50, 50, "NO Factible", color='red', fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.6))
    else:
        print("El punto ajustado pertenece a la región factible.")

    # Etiquetas
    ax.set_xlabel('A (unidades de producto A)')
    ax.set_ylabel('B (unidades de producto B)')
    
    # Leyenda
    ax.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show(block=False)
    plt.pause(2)  # Pausa para mostrar el gráfico

# Programa principal
if __name__ == "__main__":
    while True:
        # Pedir al usuario los valores de A y B
        try:
            a = float(input("Introduce la cantidad de producto A: "))
            b = float(input("Introduce la cantidad de producto B: "))
        except ValueError:
            print("Por favor, introduce valores numéricos.")
            continue

        # Calcular y mostrar el beneficio
        beneficio = funcion_costo(a, b)
        print(f"El beneficio total para A={a} y B={b} es: {beneficio}")

        # Mostrar el gráfico de la región factible
        print("\nMostrando región factible...")
        graficar_con_restricciones(a, b)

        # Preguntar al usuario si desea ajustar las restricciones o salir
        salida = input("¿Quieres ajustar las restricciones de nuevo o salir? (ajustar/salir): ").strip().lower()
        if salida == 'salir':
            print("¡Hasta luego!")
            plt.close()  # Cerrar la ventana del gráfico
            break
        elif salida == 'ajustar':
            try:
                ajuste = float(input("Introduce un nuevo valor para ajustar las restricciones (máximo permitido en A y B): "))
                if ajuste <= 0:
                    print("El ajuste debe ser mayor a 0.")
                    continue
                # Mostrar la región factible con el ajuste
                print(f"Mostrando el ajuste con A={a} y B={b}...")
                graficar_con_restricciones(a, b, ajuste)
            except ValueError:
                print("Por favor, introduce un valor numérico válido.")
                continue
        else:
            print("Opción no válida. Por favor, elige 'ajustar' o 'salir'.")
