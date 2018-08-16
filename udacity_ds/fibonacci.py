fib = {}
def get_fib(position):
    if position < 2:
        fib[position] = 1
        return 1
    else:
        if position - 1 in fib:
            fib[position] = fib[position-1] + fib[position-2]
        elif position - 2 in fib:
            fib[position] = fib[position-2] + get_fib(position-1)
        else:
            fib[position] = get_fib(position-1) + get_fib(position-2)
        return fib[position]
    return -1

"Test cases"
print get_fib(0)
print get_fib(1)
print get_fib(2)
print get_fib(3)
print get_fib(4)
print get_fib(5)
print get_fib(6)
print get_fib(9)
