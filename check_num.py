# Using the Python language, have the function CheckNums(num1,num2) take both parameters being passed and 
# return the string true if num2 is greater than num1, otherwise return the string false. 
# If the parameter values are equal to each other then return the string -1. 

def check_num(a,b):
    if a > b:
        return False
    elif b > a:
        return True
    else:
        return -1

a,b = [int(x) for x in input('Enter 2 Nos\n').split()]
print(check_num(a,b))