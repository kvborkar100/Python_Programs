# Using the JavaScript language, have the function SimpleAdding(num) add up all the numbers from 1 to num. 
# For the test cases, the parameter num will be any number from 1 to 1000.

def simple_adding(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Sum of 1 to {} is -> {}".format(num,simple_adding(num)))