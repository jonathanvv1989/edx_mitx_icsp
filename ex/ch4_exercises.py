# Exercise: square
def square(num):
    """
    num: int or float
    returns the square of num
    """
    return num**2


# Exercise: eval quadratic
def evalQuadratic(a, b, c, x):
    """
    a, b, c: int or float constants
    x: int or float, x variable of quadratic equation
    returns value of quadratic equation
    """
    return (a * x**2) + (b * x) + c


# Exercise: fourth power
def fourthPower(x):
    """
    x: int or float
    Returns x raised to the fourth power
    """
    return square(x) * square(x)


# Exercise: odd
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 == 1


# Exercise: Power function
# Iterative version
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    res = 1
    while exp > 0:
        res *= base
        exp -= 1

    return res


# Recursive version
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)


# Greatest Common Divisor (iterative version)
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    guess = min(a, b)
    while guess > 1:
        if (
            a % guess == 0 and
            b % guess == 0
        ):
            return guess
        guess -= 1

    return 1  # default answer if failed to retrieve other value


def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    Implement Euclidean Algorithm
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    '''
    ans = max(a, b) % min(a, b)
    if ans == 0:
        return min(a, b)
    else:
        return gcdRecur(min(a, b), ans)
