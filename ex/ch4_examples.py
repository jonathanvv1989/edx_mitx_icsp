# Functions as arguments
def func_a():
    print("inside func_a")


def func_b(y):
    print("inside func_b")
    return y


def func_c(z):
    print("inside func_c")
    return z()


# Variables inside and outside function
x = 5


def f(y):
    x = 1
    x += 1
    print(x)


def g(y):
    print(x)
    print(x + 1)


# Below function would generate UnboundLocalError
# def h(y):
#     x += 1


# Recursion example 1: multiplication
# Iteration by addition
def mult_iter(a, b):
    res = 0
    while b > 0:
        res += a
        b -= 1

    return res


def mult_rec(a, b):
    if b == 1:
        print("I am in base case, b is: " + str(b))
        return a
    else:
        print("I am in recursive case, b is " + str(b))
        return a + mult_rec(a, b-1)


def factorial(n):
    if n == 1:
        print("I am in base case, n is: " + str(n))
        return 1
    else:
        print("I am in recursive case, n is: " + str(n))
        return n*factorial(n-1)


# Tower of Hanoi
def tower_h(n, fr, to, spare):
    """
    n: int, size of stack to move
    from: str, starting position of the stack
    to: str, target position of the stack
    spare: str, spare position
    returns the instruction to move stack to targe spike
    """
    if n == 1:
        print("move from " + str(fr) + " to " + str(to))
    else:
        tower_h(n-1, fr, spare, to)
        tower_h(1, fr, to, spare)
        tower_h(n-1, spare, to, fr)
