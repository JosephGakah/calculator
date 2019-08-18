import calc

operation = ""
def getInput():
    print('Valid operations: + - * /')
    return input('What operation are we performing?')
    
print('Welcome to Calculator.')
print('.......................')
doLoop = True
while(doLoop):
    operation = getInput()
    if operation == '+':
        doLoop = False
    else:
        print('Invalid operation!')
    
# operation = calc.add
num1 = input('Enter num 1 \n')
num2 = input('Enter num 2 \n')
if operation == "+":
    print(calc.add(num1, num2))