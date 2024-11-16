import sys
print("Calculator.")
print("""In our calculator, you can perform the following operations: \n addition ('+'),\n substraction ('-'),\n multiplication ('*')\n and division('/').""")

permitted_operations = ["+", "-", "*", "/"]

def choose_operation():
    while True:
        operation = input(f"Type the operation you want to perform: {permitted_operations} ")
        if operation not in permitted_operations:
            print("This operation is not permitted.")
            continue
        return operation

def get_number(question):
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("You must enter a valid number.")

def addition(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("You cannot divide by zero.")
        return None

def performer_operation(first_num, second_num, operation):
    if operation == "+":
        result = addition(first_num, second_num)
    elif operation == "-":
        result = substraction(first_num, second_num)
    elif operation == "*":
        result = multiplication(first_num, second_num)
    elif operation == "/":
        result = division(first_num, second_num)
    return result

def main():
    decision = "no"
    while True:
        match decision:
            case "no":
                first_num = get_number("Type the first number: ")
                decision = "yes"
            case "yes":
                operation = choose_operation()
                second_num = get_number("Type another number: ")
                result = performer_operation(first_num, second_num, operation)
                if result == None:
                    continue
                else:
                    print(f"{first_num} {operation} {second_num} = {result}")
                    first_num = result
                    decision = input(f"""Type 'yes' to continue calculating with {result}, type 'no' to start a new calculation, or press Enter to quit: """)
            case "":
                print("Goodbye!")
                break
            case _:
                print("Incorrect command.")
                continue
main()