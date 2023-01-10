from calc_art import logo

# custom 'clear screen' function
def cls():
    print("\n" * 20)

# Calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def modulus(n1, n2):
    return n1 % n2
def square(n1, n2):
    return n1 ** n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    '%' : modulus,
    '**' : square,
}

def calculator():
    answer = 0
    cls()
    print(logo)
    num1 = float(input("What's the first number: \n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats's the next number: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print("\n")
        print("And your answer is...\n")
        print(f"{num1} {operation_symbol} {num2} = {answer}\n")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' for another calculation: ") == 'y':
            num1 = answer
            
        else:
            should_continue = False
            calculator()

    print("\nBye, asshole.\n")
            
calculator()




