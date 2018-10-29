def findFactorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

if __name__ == "__main__":
    n = int(input("Enter a number to find factorial: "))
    print("Factorial of {} : {}".format(n,findFactorial(n)))
