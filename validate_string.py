def validate(s):
    chars = list(s)
    flag = False
    if len(chars) > 2:
        for i in range(len(chars)):
            if chars[i].isalpha() and (chars[i-1] == '+' and chars[i+1] == '+'):
                flag = True
    else:
        flag = False

    if flag == True:
        print("Given string {} is VALID".format(s))
    else:
        print("Given string {} is NOT VALID".format(s))

str1 = input("Enter String to validate: ")
validate(str1)   