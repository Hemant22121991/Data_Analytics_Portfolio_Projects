# Todo : write out the other 3 functions - substract, multiply and divide.

import calc

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2): 
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#TODO add these 4 functions into a dictionary as the values. keys = "+","-","*","/"

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

#Solution with simple while loop

# cycle = True

# while cycle:
#     choice = 'y'
#     print(calc.logo)
#     num1 = float(input("What's the first number? :"))
#     while choice == 'y':
#         print("+\n-\n*\n/")
#         operand = input("Pick and operation: ")
#         if operand not in ('+','-','*','/'):
#             print("Wrong input")
#             print("\n" *50)
#             break
#         num2 = float(input("What's the next number? :"))
#         result = operations[operand](num1,num2)
#         print(f"{num1} {operand} {num2} : {result}")
#         num1 = result
#         choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
#         if choice == 'n':
#             print("\n" *50)

#Solution with function recursion

def calculator():
    should_accumulate = True
    print(calc.logo)
    num1 = float(input("What's the first number? :"))
    while should_accumulate:
        print("+\n-\n*\n/")
        operand = input("Pick and operation: ")
        if operand not in ('+','-','*','/'):
            print("Wrong input")
            print("\n" *50)
            break
        num2 = float(input("What's the next number? :"))
        result = operations[operand](num1,num2)
        print(f"{num1} {operand} {num2} : {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" *50)
            calculator()

calculator()