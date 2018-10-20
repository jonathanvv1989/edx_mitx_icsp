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


def sqrt_approx_bs(square):
    """
    input: a square
    output: square root aproximation using bisection search
    """
    # parameters
    epsilon = 0.01
    low = 1
    high = square
    nb_guesses = 0

    # Use bisection search to compute square root
    ans = (low + high)/2.0
    while abs(ans**2 - square) >= epsilon:
        print(
            "low = " + str(low) + " high = " + str(high) +
            " ans = " + str(ans)
        )
        nb_guesses += 1
        if ans**2 < square:
            low = ans
        else:
            high = ans
        ans = (low + high)/2.0

    # Print final output
    print("nb of guesses = " + str(nb_guesses))

    return ans


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
    step = 0.001
    # other variables
    nb_guesses = 0
    guess = 0.0

    # approximate cube root
    while abs(guess**3 - cube) >= epsilon and guess <= cube:
        guess += step
        nb_guesses += 1

    # display solution
    print("number of guesses: " + str(nb_guesses))
    if abs(guess**3 - cube) >= epsilon:
        return "Failed on cube root of " + str(cube)
    else:
        return guess


def dec_int_to_binary(dec_int):
    """
    input: a decimal integer
    output: binary repesentation of dec_int
    """
    # check if the int provided in negative
    if dec_int < 0:
        is_neg = True
        dec_int = abs(dec_int)
    else:
        is_neg = False
    # quick escape if the number is 0
    if dec_int == 0:
        return "0"
    # convert dec_int to binary
    res = ""
    while dec_int > 0:
        res = str(dec_int % 2) + res
        dec_int = dec_int // 2
    # final output
    if is_neg:
        res = "-" + res

    return res
