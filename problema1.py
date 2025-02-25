#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    m, n = map(int, input().split())  # m: alimentos, n: salud requerida
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    total_d = sum(D)
    sum_h = sum(H)
    
    # Asegurar que sum_h >= n (garantizado por el problema)
    max_h = max(H)
    max_j = min(n + max_h, sum_h)  # Limitar hasta sum(H) o n + max_h
    
    dp = [float('inf')] * (max_j + 1)
    dp[0] = 0
    
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
    
    print(total_d - min_d)

if __name__ == '__main__':
    main()
