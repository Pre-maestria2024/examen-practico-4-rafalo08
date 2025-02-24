#def main():

#	m, n = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    # Leemos los valores de m (salud máxima) y n (cantidad de alimentos)
    n, m = map(int, input().split())
    # Arreglo de "h" (puntos de salud que da cada alimento)
    H = list(map(int, input().split()))
    # Arreglo de "d" (dólares que da si se vende cada alimento)
    D = list(map(int, input().split()))
    
    # Paso 1: Calculamos la suma total de todos los d_i.
    total_d = sum(D)
    
    # Paso 2: Definimos la DP para un rango de 0..m en salud.
    # dp[x] = costo mínimo (en términos de suma de d_i usados) para lograr salud >= x.
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0  # costo 0 para salud 0
    
    # Paso 3: Para cada alimento, actualizamos la DP.
    for i in range(n):
        hi = H[i]
        di = D[i]
        # Recorremos en orden descendente para no reutilizar el mismo alimento en una sola iteración
        for cur_health in range(m, -1, -1):
            if dp[cur_health] != INF:
                new_health = min(cur_health + hi, m)
                new_cost = dp[cur_health] + di
                if new_cost < dp[new_health]:
                    dp[new_health] = new_cost
    
    # Paso 4: La DP en dp[m] es el costo mínimo en términos de d_i para llegar a m.
    # Por ende, lo que podemos ganar = total_d - dp[m].
    answer = total_d - dp[m]
    
    print(answer)

# Sólo para que el programa sea ejecutable como script:
if __name__ == '__main__':
    main()
