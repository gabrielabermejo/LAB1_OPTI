import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Función de costo
def funcion_costo(x, y):
    return x*3 + y*2

# Restricciones
def restricciones(x, y):
    return (x + y <= 100) and (x >= 0) and (y >= 0)

#región factible
def graficar_region_factible(ax, restricciones_vertices):
    region = Polygon(restricciones_vertices, closed=True, fill=True, edgecolor='b', alpha=0.3)
    ax.add_patch(region)

    # Graficar restricciones
    x = np.linspace(-0.2, 1.5, 400)
    
    y1 = 1 - x
    ax.plot(x, y1, label='x + y = 1', color='r')
    

    ax.axvline(x=0, color='g', linestyle='--', label='x = 0')
    

    ax.axhline(y=0, color='b', linestyle='--', label='y = 0')

def graficar_con_restricciones(ajuste=1.0):
    # Configurando los límites de las restricciones
    fig, ax = plt.subplots()
    ax.set_xlim(-0.2, 1.5)
    ax.set_ylim(-0.2, 1.5)
    ax.set_title("Región Factible con Restricciones Ajustadas")
    
    restricciones_vertices = [(0, 0), (ajuste, 0), (0, ajuste), (1, 0), (0, 1)]
    
    # Grafica región factible
    graficar_region_factible(ax, restricciones_vertices)
    
    # Etiquetas
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    

    ax.legend()
    
    #  gráfico
    plt.grid(True)
    plt.show(block=False)  # Mostrar gráfico sin bloquear el programa
    plt.pause(2)  # Pausar para permitir que el usuario vea el gráfico

# Programa principal
if __name__ == "__main__":
    # Interfaz gráfica
    print("### Evaluador de la Función de Costo ###")
    evaluar_funcion_costo()

    ajuste = 1.0  # Valor inicial de ajuste

    while True:
        # Mostrar gráfico
        print("\nMostrando región factible...")
        graficar_con_restricciones(ajuste)
        
        
        salida = input("¿Quieres ajustar las restricciones de nuevo o salir? (ajustar/salir): ").strip().lower()
        if salida == 'salir':
            print("¡Hasta luego!")
            plt.close() 
            break
        elif salida == 'ajustar':
            ajuste = float(input("Introduce un nuevo valor para ajustar las restricciones: "))
        else:
            print("Opción no válida. Por favor, elige 'ajustar' o 'salir'.")
