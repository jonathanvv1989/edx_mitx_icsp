varA = 5
varB = 5


# exercise vara varb
def vara_varb(varA, varB):
    if any([type(varA) is str, type(varB) is str]):
        return("string involved")
    elif varA > varB:
        return("bigger")
    elif varA == varB:
        return("equal")
    elif varA < varB:
        return("smaller")


# problem set 1
def vowels_counter(s):
    """
    ch2 problem 1
    count the number of vowels in s
    """
    vowels = "aeiou"
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return "Number of vowels is: " + str(count)


# problem set 2
def bob_counter(s):
    """
    ch2 problem 2
    counter the number of times 'bob' occurs
    """
    pattern = "bob"
    counter = 0
    for i in range(len(s)-2):
        if s[i:i+3] == pattern:
            counter += 1
    s_msg = "Number of times " + pattern + " occurs is: " + str(counter)

    return s_msg


# problem 3
def count_alph(s):
    """
    ch2 problem 3
    counter the longest sub-string in alphabetical order
    """
    # draft logic think 1st case, first master etc..
    master_str = ""
    sub_str = ""
    for i in range(len(s)):
        next_gt = False
        sub_str += s[i]
        if i < (len(s)-1):
            # is next letter alphabetically greater?
            if (s[i+1] >= s[i]):
                next_gt = True
        # end of consecutive string
        if not next_gt:
            if len(sub_str) > len(master_str):
                master_str = sub_str
            # reset sub string
            sub_str = ""

    return "Longest substring in alphabetical order is: " + master_str
