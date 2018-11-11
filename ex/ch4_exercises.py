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
