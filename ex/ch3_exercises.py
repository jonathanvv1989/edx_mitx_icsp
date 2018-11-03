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
    for _ in range(1, 13):
        rm_balance *= (1 + monthly_int_rate) * (1 - monthlyPaymentRate)

    return "Remaining balance: " + str(round(rm_balance, 2))


# Problem set 2
def credit_card_min_pmt_ee(balance, annualInterestRate):
    """
    Input1: balance at the start of the year
    Input2: annual interest rate charged on the balance
    Output: minimum monthly payment needed to square balance at year-end
    algorithm: basic exhaustive enumeration
    Slow algo so pmt_step is a multiple of 10
    """
    def final_balance(balance, monthly_int_rate, pmt):
        """
        Input1: balance at the begining of the period
        Input2: monthly interest rate to charge
        Input3: payment made monthly
        Ouput: final balance at the end of the year
        """
        for _ in range(1, 13):
            balance -= pmt
            balance *= (1 + monthly_int_rate)

        return balance

    monthly_int_rate = annualInterestRate/12.0
    # Implement algorithm to find allowance to repay full balance
    fin_balance = balance
    pmt = 0
    pmt_step = 10
    nb_guesses = 0
    while fin_balance > 0:
        pmt += pmt_step
        fin_balance = final_balance(balance, monthly_int_rate, pmt)
        nb_guesses += 1

    print("Guesses: " + str(nb_guesses))
    return "Lowest Payment: " + str(pmt)


# Problem set 3
def credit_card_min_pmt_bs(balance, annualInterestRate):
    """
    Input1: balance at the start of the year
    Input2: annual interest rate charged on the balance
    Output: minimum monthly payment needed to square balance at year-end
    algorithm: bisection search
    Fast algo so expected to be accurate to the $0.01
    """
    def final_balance(balance, monthly_int_rate, pmt):
        """
        Input1: balance at the begining of the period
        Input2: monthly interest rate to charge
        Input3: payment made monthly
        Ouput: final balance at the end of the year
        """
        for _ in range(1, 13):
            balance -= pmt
            balance *= (1 + monthly_int_rate)

        return balance

    # parameters
    mir = annualInterestRate/12.0
    low = balance/12.0  # if ir = 0 then mini pmt = balance / 12
    high = (balance * (1 + mir)**12)/12.0
    pmt = (low + high)/2.0
    epsilon = 0.01
    # Implement algorithm to find allowance to repay full balance
    fin_balance = balance
    nb_guesses = 0
    while abs(fin_balance) >= epsilon:
        nb_guesses += 1
        fin_balance = final_balance(balance, mir, pmt)
        # print("Low:", str(low), "High:", str(high), "Pmt:", str(pmt),
        #       "fin_bal:", str(fin_balance))
        # implement bisection search logic
        if fin_balance > 0:
            low = pmt
        else:
            high = pmt

        pmt = (low + high)/2.0

    print("Guesses: " + str(nb_guesses))
    return "Lowest Payment: " + str(round(pmt, 2))
