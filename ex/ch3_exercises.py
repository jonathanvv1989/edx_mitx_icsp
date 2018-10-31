def guess_the_nber():
    """
    small program using bisection seach to guess a number in your mind
    """
    # Paremeters
    low = 0
    high = 100
    s_input = (
        "Enter 'h' to indicate the guess is too high. " +
        "Enter 'l' to indicate the guess is too low. " +
        "Enter 'c' to indicate I guessed correctly. "
    )

    print("Please think of a number between 0 and 100!")

    ans = ""
    while ans != "c":
        # check new guess
        g = (low + high)//2
        print("Is you secret number " + str(g) + "?")
        ans = input(s_input)
        # bisection search
        if ans == "h":
            high = g
        elif ans == "l":
            low = g
        elif ans != "c":
            print("Sorry, I did not understand your input.")

    return "Game over. Your secret number was: " + str(g)


# Problem set 1
def credit_card_min_balance(
    balance,
    annualInterestRate,
    monthlyPaymentRate
):
    """
    Input1: balance at the start of the year
    Input2: annual interest rate
    Input3: mini month payment rate
    Output: final balance if only pay minimum every month
    """
    rm_balance = balance
    monthly_int_rate = annualInterestRate/12.0
    for m in range(1, 13):
        rm_balance *= (1 + monthly_int_rate) * (1 - monthlyPaymentRate)

    return "Remaining balance: " + str(round(rm_balance, 2))


# Problem set 2
# Problem set 3
