import calc

operation = ""
def getInput():
    print('Valid operations: + - * / !')
    return input('What operation are we performing?')

def main():    
    print('Welcome to Calculator.')
    print('.......................')
    doLoop = True
    while(doLoop):
        operation = getInput()
        if operation in ['+','-','/','*', '!']:
            doLoop = False
        else:
            print('Invalid operation!')
        
    # operation = calc.add
    
    if operation == '!':
        print(calc.doFactorial())

    if operation == "+":
        print(calc.add())

    if operation == "-" :
        print(calc.sub())

    if operation == "*":
        print(calc.multiply())

    if operation == "/":
        print(calc.divide())
    print('Do you wish to continue? Press any key.')
    return input('If not enter -1:')

runProgram = True
while(runProgram):
    cont = main()
    if(cont == '-1'):
        runProgram = False