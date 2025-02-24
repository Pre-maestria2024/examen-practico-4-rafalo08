#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    # Ruta del archivo de entrada
    #file_path = r"C:\Users\racueva\Desktop\problema1_input15.txt"

    # Leer la entrada desde el archivo
    #with open(file_path, "r") as file:
    #    lines = file.readlines()

    # Procesar las líneas del archivo
    m, n = map(int, input().split())  # m: número de alimentos, n: salud máxima
    H = list(map(int, input().split()))  # hi: aumento de salud por cada alimento
    D = list(map(int, input().split()))  # di: dinero obtenido si se vende el alimento

    # Crear una lista de tuplas (hi, di) para facilitar el procesamiento
    foods = [(H[i], D[i]) for i in range(m)]

    # Ordenar los alimentos por su valor monetario di de menor a mayor
    # Esto asegura que consumimos primero los alimentos menos valiosos
    foods.sort(key=lambda x: x[1])

    # Inicializar la tabla DP
    # dp[j]: Máximo dinero que se puede ganar con salud actual j
    dp = [0] * (n + 1)

    # Iterar sobre cada alimento
    for hi, di in foods:
        # Actualizar la tabla DP desde atrás hacia adelante
        for j in range(n, -1, -1):
            if j < n:
                # Si la salud no está completamente restaurada, consumir el alimento
                new_health = min(j + hi, n)
                dp[new_health] = max(dp[new_health], dp[j])
            else:
                # Si la salud ya está completamente restaurada, vender el alimento
                dp[j] = max(dp[j], dp[j] + di)

    # El resultado es el máximo dinero que se puede ganar cuando la salud es n
    print(dp[n])


# Ejecutar el programa
if __name__ == '__main__':
    main()
