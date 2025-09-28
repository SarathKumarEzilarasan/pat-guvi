# 5! -> 5*4*3*2*1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# print(factorial(5))


def factorial_recursive(n):
    # base condition
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_recursive(5))


# factorial_recursive(3)
#       3 * 2
#            2 * 1
#                  1