#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    m, n = map(int, input().split())  # m: alimentos, n: salud requerida
    H = list(map(int, input().split()))  # Incrementos de salud
    D = list(map(int, input().split()))  # Daños asociados
    
    total_d = sum(D)  # Daño total inicial
    sum_h = sum(H)    # Suma total de salud disponible
    
    # Si la suma de H es menor que n, es imposible alcanzar la salud requerida
    if sum_h < n:
        print(-1)  # Indicar que no es posible alcanzar la salud requerida
        return
    
    max_h = max(H)
    max_j = min(n + max_h, sum_h)  # Limitar hasta sum(H) o n + max_h
    
    dp = [float('inf')] * (max_j + 1)
    dp[0] = 0  # Caso base: salud 0 requiere daño 0
    
    for i in range(m):
        h = H[i]
        d = D[i]
        # Actualizar en reversa para evitar sobreposición
        for j in range(max_j, h - 1, -1):
            if dp[j - h] + d < dp[j]:
                dp[j] = dp[j - h] + d
        # Manejar casos donde h > max_j
        if h > max_j and d < dp[max_j]:
            dp[max_j] = d
    
    # Encontrar el mínimo D para salud >= n
    start = max(n, 0)
    min_d = min(dp[start:max_j + 1])
    
    # Si no se puede alcanzar la salud requerida (min_d sigue siendo infinito)
    if min_d == float('inf'):
        print(-1)  # Indicar que no es posible alcanzar la salud requerida
    else:
        print(total_d - min_d)

if __name__ == '__main__':
    main()
