"""fibonacci"""
def fibonacci(nnn):
    """fibonacci"""
    if nnn == 0:
        return 0
    elif nnn == 1 or nnn == 2:
        return 1
    else:
        return fibonacci(nnn-1) + fibonacci(nnn-2)
print(fibonacci(int(input())))
