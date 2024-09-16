import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def f_sin(x):
    return np.sin(x)

def f_cos(x):
    return np.cos(x)

def f_exp(x):
    return np.exp(x)

def f_log(x):
    return np.log(1+x)

def f_tan(x):
    return np.tan(x)

def taylor_series(func, x0, n):
    x = sp.Symbol('x')
    taylor_expansion = func.series(x, x0, n+1).removeO()
    return taylor_expansion

funciones = {
    "1": ("sin(x)", f_sin),
    "2": ("cos(x)", f_cos),
    "3": ("exp(x)", f_exp),
    "4": ("log(1+x)", f_log),
    "5": ("tan(x)", f_tan)
}

print("Selecciona una función para la expansión en serie de Taylor:")
print("1: sin(x)")
print("2: cos(x)")
print("3: exp(x)")
print("4: log(1+x)")
print("5: tan(x)")
opcion = input("Ingresa el número de la función: ")

if opcion not in funciones:
    print("Opción no válida.")
    exit()

funcion_seleccionada, funcion_python = funciones[opcion]

x0 = float(input("Ingresa el punto de expansión (x0): "))
n = int(input("Ingresa el número de términos de la serie de Taylor: "))

x_vals = np.linspace(x0 - 5, x0 + 5, 400)
y_vals = funcion_python(x_vals)

x = sp.Symbol('x')
funcion_sympy = sp.sympify(funcion_seleccionada)
taylor_expansion = taylor_series(funcion_sympy, x0, n)

taylor_funcion = sp.lambdify(x, taylor_expansion, modules=['numpy'])
y_taylor_vals = taylor_funcion(x_vals)

plt.plot(x_vals, y_vals, label=f'Función original: {funcion_seleccionada}')
plt.plot(x_vals, y_taylor_vals, '--', label=f'Aproximación Taylor (n={n})')
plt.axvline(x=x0, color='r', linestyle='--', label=f'Punto de expansión: x0={x0}')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Aproximación en Series de Taylor para {funcion_seleccionada}')
plt.grid(True)
plt.show()
