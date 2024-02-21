N = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))
dp = [0] * (N + 1)

dp[1] = 0
dp[2] = A[0]
for s in range(3, N + 1):
    dp[s] = min(dp[s - 1] + A[s - 2], dp[s - 2] + B[s - 3])

print(dp[N])
