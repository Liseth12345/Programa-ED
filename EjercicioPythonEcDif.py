#CIPA 
#linda Valentina Gonzalez Vega
#Stephanie Liseth Solano Puentes

# Se importan las librerías sympy, numpy y matplotlib
#Sympy: manejo de operaciones simbólicas
#Numpy: manejo de arreglos y operaciones numéricas
#Matplotlib.pyplot: Se utiliza para visualizar la gráfica
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Se definen las variables
x, y, C = sp.symbols('x y C')


print("¡¡Bienvenido al programa de ecuaciones diferenciales!!:D")
print("Por favor ingresa la ecuación diferencial en la forma dy/dx = f(x, y)")

# Función para ingresar la ecuación diferencial
equation = input("Ingresa la ecuación diferencial (dy/dx en términos de x y y): ")

# Convierte la ecuación a una forma simbólica
dy_dx = sp.sympify(equation)

# Separa las variables
lhs = sp.Derivative(y, x)  # dy/dx
rhs = dy_dx
separable = sp.Eq(lhs, rhs)

# Son los print para indicarle al usuario dónde agregar la información
# de la ecuación diferencial
print("\nPaso 1: Ecuación diferencial ingresada:")
print(f"dy/dx = {equation}")

# Si es separable,Integrar ambos lados
try:
    # para poder obtener la forma separable se tiene que reorganizar
    dy_dx = sp.Eq(lhs, rhs)
    
    print("\nPaso 2: Separando las variables:")
    print(f"dy/dx = {rhs}")
    
    
    # Integrar
    print("\nPaso 3: Integrando ambos lados de la ecuación:")
    integral_lhs = sp.integrate(1/y, y)
    integral_rhs = sp.integrate(rhs, x)
    
    # (Integral del lado izquierdo): integral_lhs
    # (Integral del lado derecho): integral_rhs 
    print(f"∫(1/y) dy = {integral_lhs}")
    print(f"∫f(x) dx = {integral_rhs} + C (constante de integración)")
    
    # Solución general
    general_solution = sp.Eq(integral_lhs, integral_rhs + C)
    print("\nPaso 4: La solución general de la ecuación es:")
    print(general_solution)

    # Condiciones iniciales
    x0 = float(input("\nIngresa el valor de x0 (condición inicial): "))
    y0 = float(input("Ingresa el valor de y0 (condición inicial): "))

    # Sustituye las condiciones iniciales para encontrar C
    particular_solution = general_solution.subs({x: x0, y: y0})
    print("\nPaso 5: Sustituyendo las condiciones iniciales para encontrar C:")
    print(f"Cuando x = {x0} y y = {y0}, la ecuación es: {particular_solution}")

    C_value = sp.solve(particular_solution, C)[0]
    print(f"El valor de C es: {C_value}")
    
    # Sustituye C en la solución general para conseguir la particular de las condiciones iniciales
    particular_solution = general_solution.subs(C, C_value)
    print("\nPaso 6: Solución particular con las condiciones iniciales:")
    print(particular_solution)

    # Graficar la ecuación implícita
    print("Graficando la solución implícita...")

    # Crear una malla de valores para x y y
    # Conjunto de variables de x: x_vals
    # Conjunto de variables de y: y_vals 
    # meshgrid es una herramienta poderosa en NumPy que facilita la creación de cuadrículas de coordenadas
    x_valores = np.linspace(x0 - 10, x0 + 10, 400)
    y_valores = np.linspace(0.1, y0 + 10, 400)  # Evita valores cero o negativos
    X, Y = np.meshgrid(x_valores, y_valores)
    #x_vals: se usa para generar un rango de valores para x alrededor
    #de la condición inicial x0, en el que nos permite visualizar la solución
    #en un intervalo que se extiende 10 unidades a cada lado de x0
    
    #y_vals: Nos da un rango de valores para y, en el que inicia
    #desde 0.1 para evitar problemas en el logaritmo y asimismo,
    #que pueda extenderse hasta 10 unidades por encima de y0

    # Evaluar la ecuación implícita
    Z = sp.lambdify((x, y), particular_solution.lhs - particular_solution.rhs, "numpy")(X, Y)

    # Graficar las curvas de nivel para la solución implícita
    #plt se utiliza para crear gráficos y visualizaciones en Python; Llama a la librería de matplotlib.pyplot
    plt.contour(X, Y, Z, levels=[0], colors='blue')
    plt.scatter([x0], [y0], color='red', label='Condición inicial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la solución implícita de la EDO')
    plt.legend()
    plt.grid(True)
    plt.show()   
except Exception as e:
    print(f"Error al procesar la ecuación: {e}")

print ("Fin de la ecuación")
