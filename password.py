def check(password):
    # this function takes ur password and check if its valid - by meeting some sets of conditions
    # if its valid, it saves ur password

    special_char = " ~!@#$%^&*()_+-=`\":';}{]['/.,><?"
    spec_char_in_password = False
    dgt_in_password = False
    lower_case_in_password = False
    upper_case_in_password = False

    for character in password:
        if character.isdigit():  # checks if password contains a digit
            dgt_in_password = True
        if character in special_char:  # checks if password contains a special character
            spec_char_in_password = True
        if character.islower():
            lower_case_in_password = True  # checks if password contains lower case
        if character.isupper():
            upper_case_in_password = True  # checks if password contains upper case
    if len(password) < 8:
        print(" Very Weak password: password must have at least 8 characters")
    elif lower_case_in_password == False:
        print("weak password: password must contain Lower case")
    elif not upper_case_in_password:
        print("weak password: password must contain mixed cases")
    elif not dgt_in_password:
        print("moderate password: password must contain a digit")
    elif not spec_char_in_password:
        print("strong password: consider including a special character")
    elif dgt_in_password and spec_char_in_password and lower_case_in_password and upper_case_in_password and len(password) >= 8:
            #True               #True                   #True                       #True                       #True
        print("Very Strong password: password saved ")
        #return f" your new password is : {password}"


passTxt = "hammeD1###"
check(passTxt)

