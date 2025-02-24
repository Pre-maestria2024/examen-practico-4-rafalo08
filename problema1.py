#def main():

#	n, m = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    total_D = sum(D)
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0  # Caso base: salud 0 sin usar alimentos
    
    for h, d in zip(H, D):
        # Iterar hacia atrás para evitar procesar el mismo alimento múltiples veces
        for j in range(n, -1, -1):
            if dp[j] != INF:
                new_j = min(j + h, n)
                if dp[new_j] > dp[j] + d:
                    dp[new_j] = dp[j] + d
    
    print(total_D - dp[n])

if __name__ == '__main__':
    main()
