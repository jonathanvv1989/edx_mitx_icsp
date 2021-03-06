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


def sqrt_approx_nr(square):
    """
    input: a square
    output: square root approximation using Newton-Raphson
    """
    # parameters
    epsilon = 0.01
    nb_guesses = 0

    ans = square/2.0  # same start as bs for benchmarking
    # Use Newton-Raphson to compute square root
    while abs(ans**2 - square) >= epsilon:
        nb_guesses += 1
        ans = ans - (((ans**2) - square)/(2*ans))

    # Print final output and benchmark
    print("Number of guesses: " + str(nb_guesses))
    print("Square root of " + str(square) + " is " + str(ans))

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


def dec_flt_to_binary(dec_flt):
    """
    input: a decimal float
    output: binary representation of dec_flt
    """
    # Find power of 2 converting to whole number
    p = 0
    while (dec_flt*2**p) % 1 != 0:  # not a whole number
        print("Remainder: " + str((dec_flt*2**p)-int(dec_flt*2**p)))
        p += 1

    # convert int to binary
    dec_int = int(dec_flt*2**p)
    print("Int converter is: " + str(p) + " to int: " + str(dec_int))
    res = dec_int_to_binary(dec_int)

    # shift binary to right based on power of 2 p introduced in step 1
    for _ in range(p-len(res)):  # add 0 after the decimal places
        res = '0' + res
    res = res[0:-p] + "." + res[-p:]

    return res
