#def main():

#	m, n = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    import math

    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    if len(H) < n:
        H += [0]*(n - len(H))
    if len(D) < n:
        D += [0]*(n - len(D))

    S = sum(D)

    dp = [math.inf]*(m+1)
    dp[0] = 0  

    for i in range(n):
        hi = H[i]
        di = D[i]
        
        new_dp = dp[:]
        for k in range(m+1):
            if dp[k] == math.inf:
                continue
            
            new_k = k + hi
            if new_k > m:
                new_k = m
            cost_if_eat = dp[k] + di
            if cost_if_eat < new_dp[new_k]:
                new_dp[new_k] = cost_if_eat
        dp = new_dp

    
    if dp[m] == math.inf:
        print(0)
    else:
        print(S - dp[m])  

if __name__ == '__main__':
    main()
