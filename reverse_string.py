# Question: Have the function FirstReverse(str_) take the str parameter
# being passed and return the string in reversed order.

def get_input():
    s = input("Enter the String to reverse: ")
    return s

def ReverseString(str):
    str = reversed(list(str))
    rev = ''.join(str)
    print("Reversed String is:{}".format(rev))       

if __name__ == "__main__":
    s = get_input()
    ReverseString(s)
