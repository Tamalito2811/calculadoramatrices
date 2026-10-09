# Calcular las matrices

# Definir las variaqbles n y m

print("===============================")
print("    Calculadora de matrices"    )
print("===============================")
n = int(input("Ingrese valor de n (filas): "))
m = int(input("Ingrese el valor de m (colmnas): "))
print("--------------------------------")
print("para el valor de las filas:",n)
print("Para el valor de las columnas:",m)

# Declarar la Matriz
def mostrar_matriz(titulo, M):
    print(f"\n{titulo}:")
    for fila in M:
        print(fila)

# Definir la matriz A y B

def crear_matriz(nombre):
    print(f"\n--- Ingrese los datos para la {nombre} ---")
    matriz = []
    for i in range(n):
        fila_temporal = []
        for j in range(m):
            valor = float(input(f"Ingresa los valores [{i}][{j}]: "))
            fila_temporal.append(valor)
        matriz.append(fila_temporal)
    return matriz

# Creamos los valores de Matriz A,B

matriz_A = crear_matriz("Matriz A")
matriz_B = crear_matriz("Matriz B")

# Mostrar las matrices A y B
mostrar_matriz("Matriz A", matriz_A)
mostrar_matriz("Matriz B", matriz_B)

# Creamos las variables para ( +, -, *, /)

opcion = ""

while opcion != "5":
    print("\n===================================")
    print("        MENÚ DE OPERACIONES          ")
    print("===================================")
    print("1. Sumar (A + B)")
    print("2. Restar (A - B)")
    print("3. Multiplicar (A * B)")
    print("4. Dividir (A / B)")
    print("5. Salir")

    opcion = input("\nSeleccione una opción (1-5): ")

    # OPCIÓN 1: SUMA
    if opcion == "1":
        matriz_suma = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(matriz_A[i][j] + matriz_B[i][j])
            matriz_suma.append(fila)
        mostrar_matriz("El resultado de tu matriz Suma (A + B) es:", matriz_suma)

    # OPCIÓN 2: RESTA
    elif opcion == "2":
        matriz_resta = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(matriz_A[i][j] - matriz_B[i][j])
            matriz_resta.append(fila)
        mostrar_matriz("El resultado de tu matriz Resta (A - B) es:", matriz_resta)

    # OPCIÓN 3: MULTIPLICACIÓN
    elif opcion == "3":
        matriz_mult = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(matriz_A[i][j] * matriz_B[i][j])
            matriz_mult.append(fila)
        mostrar_matriz("El resultado de tu matriz Multiplicar (A * B) es:)", matriz_mult)

    # OPCIÓN 4: DIVISIÓN
    elif opcion == "4":
        matriz_div = []
        for i in range(n):
            fila = []
            for j in range(m):
                val_b = matriz_B[i][j]
                if val_b != 0:
                    fila.append(round(matriz_A[i][j] / val_b, 2))
                else:
                    fila.append("Indefinido")
            matriz_div.append(fila)
        mostrar_matriz("El resultado de tu matriz Dividir (A / B) es:", matriz_div)

    # OPCIÓN 5: SALIR
    elif opcion == "5":
        print("\nGracias por usarme chavalin")

    # OPCIÓN INVÁLIDA
    else:
        print("\nLa opcion que escogiste nos es valida. Por favor, ingrese un número del 1 al 5.")