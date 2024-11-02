import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Función principal
def main():
    x, y = sp.symbols('x y')

    # 1. Ingresar la ecuación diferencial
    ecuacion_diferencial = input("Ingrese la ecuación diferencial en forma M(x,y)dx + N(x,y)dy = 0 (ejemplo: x**2 + y**2, 2*x*y): ")
    M_expr, N_expr = ecuacion_diferencial.split(',')
    
    # Convertir las expresiones a formato simbólico
    M = sp.sympify(M_expr.strip())
    N = sp.sympify(N_expr.strip())
    
    # Validar que las expresiones contengan las variables x e y
    if not (M.has(x, y) and N.has(x, y)):
        print("Error: M(x, y) y N(x, y) deben depender de x e y.")
        return

    # 2. Identificar si es una ecuación diferencial exacta
    if not verificar_exactitud(M, N):
        print("Lo siento, esta ecuación no es exacta.")
        factor_integrante = calcular_factor_integrante(M, N)
        print(f"Factor integrante: {factor_integrante}")
        return

    # 3. Si es exacta, pedir la condición inicial
    x0 = float(input("Ingrese el valor de la condición inicial x0: "))
    y0 = float(input("Ingrese el valor de la condición inicial y0: "))

    # 4. Resolver la ecuación exacta
    solucion_general, solucion_particular = resolver_exacta(M, N, x0, y0)

    # 5. Mostrar la solución
    print(f"La ecuación es exacta.")
    print(f"La solución dada a la condición inicial es: y = {solucion_particular}")
    
    # Mostrar la solución general de forma más clara
    print(f"La solución general es: F(x, y) = {solucion_general} = C")
    
    # 6. Configuración y generación de la gráfica
    x_min = -10  # Valor predeterminado
    x_max = 10   # Valor predeterminado
    y_min = -10  # Valor predeterminado
    y_max = 10   # Valor predeterminado
    densidad = 100  # Valor predeterminado

    # Graficar la solución particular
    graficar_solucion(solucion_particular, x0, y0, x_min, x_max, y_min, y_max, densidad)

# Función para verificar si la ecuación es exacta
def verificar_exactitud(M, N):
    x, y = sp.symbols('x y')
    dM_dy = sp.diff(M, y)  # Derivada parcial de M respecto a y
    dN_dx = sp.diff(N, x)  # Derivada parcial de N respecto a x
    return dM_dy == dN_dx

# Función para calcular el factor integrante (esbozo)
def calcular_factor_integrante(M, N):
    # Implementar el cálculo del factor integrante aquí si es necesario
    return None

# Función para resolver una ecuación diferencial exacta
def resolver_exacta(M, N, x0, y0):
    x, y = sp.symbols('x y')
    
    # Integra M respecto a x
    F = sp.integrate(M, x)
    
    # Encuentra la función de y faltante en F
    G_y = N - sp.diff(F, y)
    G = sp.integrate(G_y, y)
    
    # Solución general
    F += G
    solucion = F + sp.symbols('C')
    
    # Usar la condición inicial para encontrar C
    C_valor = sp.solve(solucion.subs({x: x0, y: y0}), sp.symbols('C'))[0]
    solucion_particular = solucion.subs(sp.symbols('C'), C_valor)
    
    return solucion, solucion_particular

# Función para graficar la solución
def graficar_solucion(solucion, x0, y0, x_min=-10, x_max=10, y_min=-10, y_max=10, densidad=100):
    x, y = sp.symbols('x y')
    f_lambdified = sp.lambdify((x, y), solucion, 'numpy')
    
    x_valores = np.linspace(x_min, x_max, densidad)
    y_valores = np.linspace(y_min, y_max, densidad)
    X, Y = np.meshgrid(x_valores, y_valores)
    Z = f_lambdified(X, Y)
    
    plt.contour(X, Y, Z, levels=[0], colors='b')
    plt.plot(x0, y0, 'ro')  # Mostrar la condición inicial
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Curva de nivel de la solución particular")
    plt.grid()
    plt.show()

# Ejecutar el programa
main()
