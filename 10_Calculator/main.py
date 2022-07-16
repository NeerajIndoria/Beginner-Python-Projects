from art import logo
def add(number1,number2):
  return number1+number2

def mul(number1,number2):
  return number1*number2

def div(number1,number2):
  return number1/number2

def sub(number1,number2):
  return number1-number2

operations= {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:    
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if choice == 'n':
            should_continue = False
            calculator()
        num1 = result

calculator()