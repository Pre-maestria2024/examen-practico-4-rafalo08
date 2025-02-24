#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    # 1) Leer n y m
    n, m = map(int, input().split())
    
    # 2) Leer el arreglo H (n valores)
    H = list(map(int, input().split()))
    
    # 3) Leer el arreglo D (n valores)
    D = list(map(int, input().split()))
    
    # 4) Suma total de los d_i (si vendiéramos todos los alimentos)
    total_d = sum(D)
    
    # 5) Definir el arreglo dp para la salud de 0 hasta m
    #    dp[x] = costo mínimo (suma de d_i de alimentos comidos) para conseguir salud >= x
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0  # Para salud 0, no se necesita comer nada (costo=0)
    
    # 6) Lógica de la DP: actualizar para cada alimento
    for i in range(n):
        hi = H[i]
        di = D[i]
        # Recorremos la salud en orden descendente para evitar
        # reutilizar el mismo alimento varias veces en una sola pasada
        for cur_health in range(m, -1, -1):
            if dp[cur_health] != INF:
                new_health = cur_health + hi
                if new_health > m:
                    new_health = m
                new_cost = dp[cur_health] + di
                if new_cost < dp[new_health]:
                    dp[new_health] = new_cost
    
    # 7) dp[m] indica la suma mínima de d_i de los alimentos que se debieron comer
    answer = total_d - dp[m]
    print(answer)


if __name__ == '__main__':
    main()
