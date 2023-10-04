
def calc_fib(n, hold):
    if n in hold:
        return hold[n]

    if n <= 2:
        return 1

    result = calc_fib(n - 1, hold) + calc_fib(n - 2, hold)
    hold[n] = result
    return result


line = int(input())
print(calc_fib(line, {}))