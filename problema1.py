#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    # 1) Leer n y m
    n, m = map(int, input().split())
    
    # 2) Leer los arreglos H y D, cada uno con n elementos
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    # 3) Calcular la suma total de D (dinero si vendiéramos todo)
    total_d = sum(D)
    
    # 4) dp[x] = costo mínimo (en d_i) para lograr salud >= x
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0
    
    # 5) Actualizar la DP con cada alimento
    for i in range(n):
        hi = H[i]
        di = D[i]
        # Recorremos salud en orden descendente
        for cur_health in range(m, -1, -1):
            if dp[cur_health] != INF:
                new_health = cur_health + hi
                if new_health > m:
                    new_health = m
                new_cost = dp[cur_health] + di
                if new_cost < dp[new_health]:
                    dp[new_health] = new_cost
    
    # 6) dp[m] es el costo total mínimo de los alimentos “consumidos”
    #    para llegar a salud m. La ganancia es lo que dejamos de “consumir”
    answer = total_d - dp[m]
    print(answer)

if __name__ == '__main__':
    main()
