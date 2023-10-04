
def bionomial(n, k, memo):
    key = f"{n} {k}"
    if key in memo:
        return memo[key]

    if k == 0 or n == k or n == 0:
        return 1

    result = bionomial(n - 1, k - 1, memo) + bionomial(n - 1, k, memo)
    memo[key] = result
    return result


n = int(input())
k = int(input())

print(bionomial(n, k, {}))
