
# def fibonacci(n):
#     if n <= 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = int(input())
#
# print(fibonacci(n))


def iteration_solution(n):
    fib0 = 1
    fib1 = 1

    result = 0
    for i in range(n - 1):
        result = (fib0 + fib1)
        fib0, fib1 = fib1, result

    return result


n = int(input())
print(iteration_solution(n))