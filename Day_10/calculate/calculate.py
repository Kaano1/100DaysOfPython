from art import logo

def add(p1, p2):
    return (p1 + p2)

def substract(p1, p2):
    return (p1 - p2)

def	multiply(p1, p2):
    return (p1 * p2)

def divide(p1, p2):
    return (p1 / p2)

def calculator():
    operations = {'*': multiply, '+': add, '-': substract, '/':divide}

    num1 = float( input("What's the first number?\n") )

    print("\n")
    for pr in operations:
        print(pr)
    
    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float( input("What's the second number?\n") )

    func = operations[operation_symbol]
    answer = func(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    condition = True

    answer2 = answer
    while condition:
        if (input(f"Type 'y' continue calculation with {answer2}, or type 'n' to exit.: ") == 'y'):
            operation_symbol = input("Pick an operation from the line above: ")
            num2 = float( input("What's the next number? ") )
            func = operations[operation_symbol]
            answer2 = func(answer, num2)
            print(f"{answer} {operation_symbol} {num2} = {answer2}")
            condition = True
        else:
            condition = False
            calculator()
print(logo)
calculator()