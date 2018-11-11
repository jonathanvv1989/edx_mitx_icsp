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
