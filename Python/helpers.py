fib_dict = {}


def fib_memo(n):
    if n in fib_dict:
        return fib_dict[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    fib_dict[n] = result
    return result