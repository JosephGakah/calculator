def add():
    num1 = int(input('Enter num 1 \n'),10)
    num2 = int(input('Enter num 2 \n'),10)
    return num1 + num2

def addWithParams(a, b):
    return a + b

def sub() :
    num1 = int(input('Enter num 1 \n'),10)
    num2 = int(input('Enter num 2 \n'),10)
    return num1 - num2 

def multiply() :
    num1 = int(input('Enter num 1 \n'),10)
    num2 = int(input('Enter num 2 \n'),10)
    return num1 * num2 

def divide():
    num1 = int(input('Enter num 1 \n'),10)
    num2 = int(input('Enter num 2 \n'),10)
    return num1 // num2

def doFactorial():
    num = int(input('Enter the number \n'), 10)
    return factorial(num)

def factorial(num):
    if num == 0:
        return 0
    else:
        return num + factorial(num - 1)
