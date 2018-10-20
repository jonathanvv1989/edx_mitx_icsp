# Square root algorithm v1
def sqrt_int(x):
    """
    Returns the square root of x
    """
    ans = 0
    neg_flag = False

    # neg flag to display final result correctly
    if x < 0:
        neg_flag = True

    # basic guess and check algorithm
    while ans**2 < x:
        ans += 1

    if ans**2 == x:
        return ans
    else:
        if neg_flag:
            return "cannot compute negative square"
        else:
            return "not a perfect square"


def a_an_trick(a_string, e_level):
    """
    input1: word to cheer for
    input2: level of enthusiasm
    output: function cheers for you and returns boolean
    """
    # escape if input not a string
    if type(a_string) != str:
        return False

    # Proceed to main function
    an_letters = "aefhimnorsxAEFHIMNORSX"
    i = 0

    while i < len(a_string):
        char = a_string[i]
        if char in an_letters:
            # 'an' words
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a " + char + "! " + char)
        i += 1

    print("What does it spell?")
    for i in range(e_level):
        print(a_string + "!!!")

    return True


def cube_root_approx(cube):
    """
    input: a cube
    output: approximate cube root
    """
    # parameters
    epsilon = 0.01
    increment = 0.0001
    # other variables
    nb_guesses = 0
    guess = 0.0

    # approximate cube root
    while abs(guess**3 - cube) <= epsilon:
        guess += increment
        nb_guesses += 1

    # display solution
    print("number of guesses: " + str(nb_guesses))
    if abs(guess**3 - cube) >= epsilon:
        return "Failed on cube root of " + str(cube)
    else:
        return guess
