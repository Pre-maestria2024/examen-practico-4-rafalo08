#def main():

#	m, n = map(int, input().split())
#	H = list(map(int, input().split()))
#	D = list(map(int, input().split()))
	
#if __name__ == '__main__':
#	main()
def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    
    if len(H) < n:
        H += [0]*(n - len(H))
    if len(D) < n:
        D += [0]*(n - len(D))

    total_d = sum(D)

    candidatos = []
    for i in range(n):
        if H[i] >= m:
            candidatos.append(D[i])

    if candidatos:
        d_usado = max(candidatos)
        print(total_d - d_usado)
    else:
        import math
        dp = [math.inf]*(m+1)
        dp[0] = 0
        for i in range(n):
            hi, di = H[i], D[i]
            new_dp = dp[:]
            for k in range(m+1):
                if dp[k] == math.inf:
                    continue
                nk = min(m, k+hi)
                cost = dp[k] + di
                if cost < new_dp[nk]:
                    new_dp[nk] = cost
            dp = new_dp
        if dp[m] == math.inf:
            print(0)
        else:
            print(total_d - dp[m])

if __name__ == '__main__':
    main()
