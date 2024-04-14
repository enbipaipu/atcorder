N, A, B = map(int, input().split())

is_first = True

dp = [None] * (N + 1)

for i in range(N + 1):
    if i >= A and dp[i - A] is False:
        dp[i] = True
    elif i >= B and dp[i - B] is False:
        dp[i] = True

    else:
        dp[i] = False

print("First" if is_first else "Second")
