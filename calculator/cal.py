import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b  
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    number1=float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation: ") #+
        number2=float(input("Enter next number:"))
        calculator_function=operations_dict[op_symbol] #add
        ouput=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {ouput}")
        
        
        should_continue=input("Enter 'y' to continue calculation with {ouput} or 'n' to start new calculation or 'x' to exit").lower()
        if should_continue=='y':
            number1=ouput
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()   
        else:
            continue_flag=False
            print("Bye")
calculator()          

       



