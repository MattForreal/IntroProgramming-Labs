# Program to calculate the fibonacci sequence up to a number input by the user

stop = int(input("Enter a number to see the Fibonacci sequence up to that number: "))

num1 = 0
num2 = 1
count = 0

while count < stop:
    print(num2)
    numth = num1 + num2
    num1 = num2
    num2 = numth
   
    count += 1
    


