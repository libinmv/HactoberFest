# Sum of all the digits of a number -> int
def sumdigit(n):
    s = 0
    while(n):
        s += n % 10
        n //= 10
    return s
